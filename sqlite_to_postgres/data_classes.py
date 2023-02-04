import uuid
from dataclasses import dataclass, field


@dataclass
class FilmWork:
    title: str
    description: str
    creation_date: str
    file_path = str
    type: str
    created_at: str
    updated_at: str
    rating: float = field(default=0.0)
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Person:
    full_name: str
    created_at: str
    updated_at: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Genre:
    name: str
    description: str
    created_at: str
    updated_at: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class PersonFilmWork:
    role: str
    created_at: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_id: uuid.UUID = field(default_factory=uuid.uuid4)
    person_id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class GenreFilmWork:
    created_at: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    genre_id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_id: uuid.UUID = field(default_factory=uuid.uuid4)


print()

data = {'person': [
        Person('Василий Васильевич', '12-05-2001', '12-10-2001',
               'b8531efb-c49d-4111-803f-725c3abc0f5e'),
        Person('Василий Васильевич', '12-05-2001',
               '12-10-2001',
               'b8531efb-c49d-4111-45665-725c3ab0f5e')
    ],

    }
# attr_table = ', '.join(Person.__annotations__)
# for key, value in enumerate( data['person'][0].__dict__.items()):
#     print(key, value)
# print(data['person'][0].__dict__.values())
# for table in data:
#     for row in data[table]:
#         attr_table = ', '.join(row.__dict__)
#         count_args = len(row.__dict__)
#         mogrify_arg = "%s, " * count_args
#         args = ','.join(
#             cursor.mogrify(f"({mogrify_arg})", item).decode() for item in
#             row.values())
#
#
# print(f"""
#                     INSERT INTO content.temp_table ({attr_table})
#                     VALUES
#                     """)  # Исправить загружаемые таблицы)qq
# print(len(Person.__annotations__))