# import sqlite3
# from contextlib import contextmanager
# import pprint
# import json
# from data_classes import Genre, FilmWork, PersonFilmWork, Person, GenreFilmWork
# import psycopg2
#
#
# @contextmanager
# def conn_context(db_path: str):
#     conn = sqlite3.connect(db_path)
#     conn.row_factory = sqlite3.Row
#     yield conn  # С конструкцией yield вы познакомитесь в следующем модуле
#     # Пока воспринимайте её как return, после которого код может продолжить выполняться дальше
#     conn.close()
#
# #
# db_path = '../db.sqlite'
# table_name = ['film_work', 'genre', 'person', 'person_film_work',
#               'genre_film_work']
#
#
# def dict_factory(list_table):
#     data = {}
#     for key in list_table:
#         data[key] = []
#     return data
#
#
# with conn_context(db_path) as conn:
#     curs = conn.cursor()
#     data = dict_factory(table_name)
#     for table in data:
#         list_table = []
#         # Reading table
#         curs.execute(f"SELECT * FROM {table}")
#         result = curs.fetchall()
#         for row in result:
#             # Reading rows
#             list_table.append(dict(row))
#         data[table] = list_table
#
#         #
#         json_file = json.dumps(data, indent=4)
#     with open('some1.json', 'w') as file:
#         file.writelines(json_file)
# dsn = {
#     'dbname': 'movies_database',
#     'user': 'app',
#     'password': '123qwe',
#     'host': 'localhost',
#     'port': 5432,
#     'options': '-c search_path=content',
# }
#
# with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
#     data_insert = tuple(data['genre_film_work'][1].values())
#     cursor.execute(
#         "INSERT INTO content.genre_film_work (id, film_work_id, genre_id, created_at) VALUES (%s, %s, %s, %s)",
#         data_insert
#     )
#
#
# class SQLiteExtractor:
#     def __init__(self, connection: sqlite3.Connection):
#         self.__con = connection
#
#     @staticmethod
#     def dict_factory(table_names: list) -> dict:
#         data = {}
#         for key in table_names:
#             data[key] = []
#         return data
#
#     def extract_movies(self):
#         curs = self.__con.cursor()
#         data = Data()
#         for table, obj in data.__annotations__.items():
#             list_table = []
#             # Reading table
#             curs.execute(f"SELECT * FROM {table}")
#             result = curs.fetchall()
#             for row in result:
#                 # Reading rows
#                 list_table.append(obj(dict(row)))
#             data.table = list_table
#         return data
#
#
import io

import psycopg2

from sqlite_to_postgres.data_classes import Person

dsn = {
    'dbname': 'movies_database',
    'user': 'app',
    'password': '123qwe',
    'host': 'localhost',
    'port': 5432,
    'options': '-c search_path=content',
}

with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
    # Очищаем таблицу в БД, чтобы загружать данные в пустую таблицу
    # cursor.execute("""TRUNCATE content.temp_table""")

    data = {'temp_table': [
        Person('Василий Васильевич', '12-05-2001', '12-10-2001',
               'b8531efb-c49d-4111-803f-725c3abc0f5e'),
        Person('Василий Васильевич', '12-05-2001',
               '12-10-2001',
               'b8531efb-c49d-4111-45665-725c3ab0f5e')
    ],

    }
    for table in data:
        for row in data[table]:
            attr_table = ','.join(row.__dict__)
            count_args = len(row.__dict__)
            mogrify_arg = "%s, " * count_args
            args = ','.join(
                cursor.mogrify(f"({mogrify_arg})", *item.__dict__).decode() for item in
                row
            )
        cursor.execute(f"""
                            INSERT INTO content.temp_table ({attr_table}) 
                            VALUES {args}
                            """)

    #TODO какие-то ошибки. Нужно преобразовать словарь в SQL запрос и отправить в временную таблицу.
    # Преобразовать таблицу под данные что выше.
    # После чего интегрировать  в основной класс