import sqlite3
from contextlib import contextmanager
import pprint
import json
from data_classes import Data
import psycopg2


@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn  # С конструкцией yield вы познакомитесь в следующем модуле
    # Пока воспринимайте её как return, после которого код может продолжить выполняться дальше
    conn.close()


db_path = 'db.sqlite'
table_name = ['film_work', 'genre', 'person', 'person_film_work',
              'genre_film_work']


def dict_factory(list_table):
    data = {}
    for key in list_table:
        data[key] = []
    return data


with conn_context(db_path) as conn:
    curs = conn.cursor()
    data = dict_factory(table_name)
    for table in data:
        list_table = []
        # Reading table
        curs.execute(f"SELECT * FROM {table}")
        result = curs.fetchall()
        for row in result:
            # Reading rows
            list_table.append(dict(row))
        data[table] = list_table

        #
        json_file = json.dumps(data, indent=4)
    with open('some1.json', 'w') as file:
        file.writelines(json_file)
dsn = {
    'dbname': 'movies_database',
    'user': 'app',
    'password': '123qwe',
    'host': 'localhost',
    'port': 5432,
    'options': '-c search_path=content',
}

with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
    data_insert = tuple(data['genre_film_work'][1].values())
    cursor.execute(
        "INSERT INTO content.genre_film_work (id, film_work_id, genre_id, created_at) VALUES (%s, %s, %s, %s)",
        data_insert
    )


class SQLiteExtractor:
    def __init__(self, connection: sqlite3.Connection):
        self.__con = connection

    @staticmethod
    def dict_factory(table_names: list) -> dict:
        data = {}
        for key in table_names:
            data[key] = []
        return data

    def extract_movies(self):
        curs = self.__con.cursor()
        data = Data()
        for table, obj in data.__annotations__.items():
            list_table = []
            # Reading table
            curs.execute(f"SELECT * FROM {table}")
            result = curs.fetchall()
            for row in result:
                # Reading rows
                list_table.append(obj(dict(row)))
            data.table = list_table
        return data

with conn_context(db_path) as conn:
    curs = conn.cursor()
