import os
from dotenv import load_dotenv

import psycopg2
from psycopg2.extras import DictCursor

from sqlite_to_postgres.load_data import sqlite3_con, load_from_sqlite

load_dotenv()

if __name__ == '__main__':
    db_path = 'db.sqlite'

    dsl = {'dbname': os.environ.get("DB_NAME"),
           'user': os.environ.get('DB_USER'),
           'password': os.environ.get('DB_PASSWORD'),
           'host': '127.0.0.1',
           'port': 5432
           }
    with sqlite3_con('db.sqlite') as sqlite_conn, \
            psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
