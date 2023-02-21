import os
import sqlite3
from contextlib import contextmanager

import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import DictCursor

from sqlite_to_postgres.load_data import load_from_sqlite

load_dotenv()


@contextmanager
def sqlite3_con(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


@contextmanager
def pg_conn(dsl, cursor_factory):
    conn = psycopg2.connect(**dsl, cursor_factory=cursor_factory)
    yield conn
    conn.close()


if __name__ == '__main__':
    db_path = 'db.sqlite'

    dsl = {'dbname': os.environ.get("DB_NAME"),
           'user': os.environ.get('DB_USER'),
           'password': os.environ.get('DB_PASSWORD'),
           'host': '127.0.0.1',
           'port': 5432
           }
    with sqlite3_con('db.sqlite') as sqlite_conn, \
            pg_conn(dsl, cursor_factory=DictCursor) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
