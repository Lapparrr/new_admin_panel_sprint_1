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


@dataclass
class Data:
    person: Person = field(default_factory=list)
    genre: Genre = field(default_factory=list)
    person_film_work: PersonFilmWork = field(default_factory=list)
    genre_film_work: GenreFilmWork = field(default_factory=list)
    film_work: FilmWork = field(default_factory=list)
