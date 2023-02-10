import sqlite3
from contextlib import contextmanager
from typing import Type

from psycopg2.extensions import connection as _connection
from sqlite_to_postgres.data_classes import Genre, PersonFilmWork, Person, \
    GenreFilmWork, FilmWork


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
        for table, value in data.items():
            table_attr = ','.join(value[0].__dict__.keys())
            mogrify_arg = ','.join('%s' for i in value[0].__dict__)
            args = ','.join(
                cursor.mogrify(f"({mogrify_arg})",
                               tuple(item.__dict__.values())).decode() for item
                in value)
            print(table_attr, mogrify_arg)
            cursor.execute(f"""INSERT INTO content.{table} ({table_attr})
                                VALUES {args}
                ON CONFLICT (id) DO NOTHING
                """)
        print('Загрузка завершена')


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
        type_data: Type[
            Genre | PersonFilmWork | Person | GenreFilmWork | FilmWork]
        for table, type_data in self.table_dataclass.items():
            curs.execute(f"SELECT * FROM {table}")
            data_value = []
            result = curs.fetchall()
            row: object
            for row in result:
                data_value.append(type_data(*tuple(row)))
            data[table] = data_value.copy()
        return data


def load_from_sqlite(connection: sqlite3.Connection,
                     pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_conn)
    sqlite_extractor = SQLiteExtractor(connection)

    data = sqlite_extractor.extract_movies()
    postgres_saver.save_all_data(data)
