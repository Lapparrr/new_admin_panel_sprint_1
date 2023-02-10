import sqlite3
from contextlib import contextmanager

import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor
from data_classes import Genre, FilmWork, PersonFilmWork, Person, GenreFilmWork


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

    def save_all_data(self, data: dict):
        cursor = self.__pg_conn.cursor()
        # Выгрузка таблицы Person
        person = data['person']
        # [obj1, ...,]
        mogrify_arg = ','.join('%s' for i in person[0].__dict__)
        print(person[0].__dict__.values())
        args = ','.join(
            cursor.mogrify(f"({mogrify_arg})",tuple(item.__dict__.values())).decode() for item in
            person)
        print(args)
        cursor.execute(f"""INSERT INTO content.person (id, full_name, created_at, updated_at)
                            VALUES {args}
            ON CONFLICT (id) DO UPDATE SET full_name=EXCLUDED.full_name
            """)
        print('Загрузка завершена')
        # Выгрузка таблицы Genre

        # Выгрузка таблицы person_film_work
        # Выгрузка таблицы genre_film_work
        # Выгрузка таблицы film_work


class SQLiteExtractor:
    table_dataclass = {"person": Person,
                       "genre": Genre,
                       "person_film_work": PersonFilmWork,
                       "genre_film_work": GenreFilmWork,
                       "film_work": FilmWork,
                       }

    def __init__(self, connection: sqlite3.Connection):
        self.__con = connection

    def extract_movies(self) -> dict:
        data = {}
        curs = self.__con.cursor()
        for table, class_obj in self.table_dataclass.items():
            curs.execute(f"SELECT * FROM {table}")
            list_obj = []
            result = curs.fetchall()
            row: object
            for row in result:
                # print(tuple(row))
                list_obj.append(class_obj(*tuple(row)))
            data[table] = list_obj.copy()
        print(data)
        return data
        # data = {table_name: [obj_data_class, ...], ... }


def load_from_sqlite(connection: sqlite3.Connection,
                     pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_conn)
    sqlite_extractor = SQLiteExtractor(connection)

    data = sqlite_extractor.extract_movies()
    postgres_saver.save_all_data(data)
