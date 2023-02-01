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
    person_id: Person.id
    film_id: FilmWork.id
    created_at: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class GenreFilmWork:
    film_id: FilmWork.id
    genre_id: Genre.id
    created_at: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Data:
    film_work: list  # FilmWork
    person: list  # Person
    genre: list  # Genre
    person_film_work: list  # PersonFilmWork
    genre_film_work: list  # GenreFilmWork
