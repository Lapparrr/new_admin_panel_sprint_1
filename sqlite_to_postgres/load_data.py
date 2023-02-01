import sqlite3
from contextlib import contextmanager

import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

from data_classes import Data


@contextmanager
def sqlite3_con(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


class PostgresSaver:
    INSERT_SIZE = 5

    def __init__(self, pg_conn: _connection):
        self.__pg_conn = pg_conn

    def save_all_data(self, data: Data):
        pass


class SQLiteExtractor:
    def __init__(self, connection: sqlite3.Connection):
        self.__con = connection

    @staticmethod
    def dict_factory(table_names: list) -> dict:
        data = {}
        for key in table_names:
            data[key] = []
        return data

    def extract_movies(self, table_names: list):
        #TODO создать объекты датаклассов и в них сохранять данные с таблиц
        curs = self.__con.cursor()
        data = self.dict_factory(table_names)
        for table in data:
            list_table = []
            # Reading table
            curs.execute(f"SELECT * FROM {table}")
            result = curs.fetchall()
            for row in result:
                # Reading rows
                list_table.append(dict(row))
            data[table] = list_table
        return data


db_path = 'db.sqlite'
table_names = ['film_work', 'genre', 'person', 'person_film_work',
               'genre_film_work']



def load_from_sqlite(connection: sqlite3.Connection,
                     pg_conn: _connection, table_names
                     ):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_conn)
    sqlite_extractor = SQLiteExtractor(connection)

    data = sqlite_extractor.extract_movies(table_names)
    postgres_saver.save_all_data(data)


if __name__ == '__main__':
    table_name = ['film_work', 'genre', 'person', 'person ']
    dsl = dict(dbname='movies_database',
               user='app',
               password='123qwe',
               host='127.0.0.1',
               port=5432
               )
    with sqlite3_con('db.sqlite') as sqlite_conn, \
            psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn, table_name)
