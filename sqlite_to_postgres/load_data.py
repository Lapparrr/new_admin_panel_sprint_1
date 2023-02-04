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

    def save_all_data(self, data: list):
        cursor = self.__pg_conn.cursor()

        data = {'person': [
            Person('Василий Васильевич', '12-05-2001', '12-10-2001',
                   'b8531efb-c49d-4111-803f-725c3abc0f5e'),
            Person('Василий Васильевич', '12-05-2001',
                   '12-10-2001',
                   'b8531efb-c49d-4111-45665-725c3ab0f5e')
        ],

        }
        attr_table = ['']
        count_args = len(data[0])
        mogrify_arg = "%s, " * count_args
        args = ','.join(
            cursor.mogrify(f"({mogrify_arg})", item).decode() for item in data)
        cursor.execute(f"""
                INSERT INTO content.temp_table (id, name) 
                VALUES {args}
                """)  # Исправить загружаемые таблицы


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
            for row in result:
                for attr in class_obj.__annotations__:
                    class_obj.attr = row[attr]
                list_obj.append(class_obj)
            data[table] = list_obj.copy()
        return data
        # data = {table_name: [obj_data_class, ...], ... }


def load_from_sqlite(connection: sqlite3.Connection,
                     pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_conn)
    sqlite_extractor = SQLiteExtractor(connection)

    data = sqlite_extractor.extract_movies()
    postgres_saver.save_all_data(data)
