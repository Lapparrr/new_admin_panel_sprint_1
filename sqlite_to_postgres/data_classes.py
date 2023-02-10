import uuid
from dataclasses import dataclass, field


@dataclass
class FilmWork:
    title: str = ''
    description: str = ''
    creation_date: str = ''
    file_path: str = ''
    rating: float = field(default=0.0)
    type: str = ''
    created_at: str = ''
    updated_at: str = ''
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Person:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    full_name: str = field(default='')
    created_at: str = ''
    updated_at: str = ''


@dataclass
class Genre:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    name: str = ''
    description: str = ''
    created_at: str = ''
    updated_at: str = ''


@dataclass
class PersonFilmWork:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_work_id: uuid.UUID = field(default_factory=uuid.uuid4)
    person_id: uuid.UUID = field(default_factory=uuid.uuid4)
    role: str = ''
    created_at: str = ''


@dataclass
class GenreFilmWork:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_work_id: uuid.UUID = field(default_factory=uuid.uuid4)
    genre_id: uuid.UUID = field(default_factory=uuid.uuid4)
<<<<<<< HEAD
    created_at: str = ''
=======
    film_id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: str
>>>>>>> 5ca85406c8694e2da897ab1d239c54ad6def1dd1

