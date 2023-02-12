import psycopg2
from psycopg2.extras import DictCursor

from sqlite_to_postgres.load_data import sqlite3_con, PostgresSaver, \
    SQLiteExtractor

db_path = '../../sqlite_to_postgres/db.sqlite'
dsl = {'dbname': 'movies_database',
       'user': 'app',
       'password': '123qwe',
       'host': '127.0.0.1',
       'port': 5432
       }
table_plural = ['film_work', 'genre', 'person', 'person ']


def test_sqlite_postgres():
    with sqlite3_con(db_path) as sqlite_conn, \
            psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
        sqlite_curs = sqlite_conn.cursor()
        pg_curs = pg_conn.cursor()
        for table_name in table_plural:
            sqlite_curs.execute(f"SELECT COUNT(*) FROM {table_name}")
            rez = sqlite_curs.fetchall()
            pg_curs.execute(f"SELECT COUNT(*) FROM content.{table_name}")
            rez_pg = pg_curs.fetchall()
            print(f'Количество строк совпадает в таблице {table_name}')
            assert list(rez[0]) == rez_pg[0]


def test_number_2():
    with sqlite3_con(db_path) as sqlite_conn, \
            psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
        sqlite_exstract = SQLiteExtractor(sqlite_conn)
        pg_exstarct = PostgresSaver(pg_conn)
        data_lite = sqlite_exstract.extract_movies()
        data_pg = pg_exstarct.extract_movies()
        for table, values in data_pg.items():
            for iter, row_pg in enumerate(values):
                data = data_lite[table][iter]
                assert row_pg == data
