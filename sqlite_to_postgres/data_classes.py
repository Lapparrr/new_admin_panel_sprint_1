import uuid
from dataclasses import dataclass, field
from datetime import datetime

dt_format = '%Y-%m-%d %H:%M:%S.%f%z'


@dataclass
class FilmWork:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    title: str = ''
    description: str = field(default='')
    creation_date: str = ''
    file_path: str = ''
    rating: float = field(default=0.0)
    type: str = ''
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at += '00'
            self.created_at = datetime.strptime(self.created_at, dt_format)
        if isinstance(self.updated_at, str):
            self.updated_at += '00'
            self.updated_at = datetime.strptime(self.updated_at, dt_format)
        if self.description is None:
            self.description = ''
        if self.file_path is None:
            self.file_path = ''


@dataclass
class Person:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    full_name: str = field(default='')
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at += '00'
            self.created_at = datetime.strptime(self.created_at, dt_format)
        if isinstance(self.updated_at, str):
            self.updated_at += '00'
            self.updated_at = datetime.strptime(self.updated_at, dt_format)


@dataclass
class Genre:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    name: str = ''
    description: str = ''
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at += '00'
            self.created_at = datetime.strptime(self.created_at, dt_format)
        if isinstance(self.updated_at, str):
            self.updated_at += '00'
            self.updated_at = datetime.strptime(self.updated_at, dt_format)
        if self.description is None:
            self.description = ''


@dataclass
class PersonFilmWork:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_work_id: uuid.UUID = field(default_factory=uuid.uuid4)
    person_id: uuid.UUID = field(default_factory=uuid.uuid4)
    role: str = ''
    created_at: datetime = datetime.now()

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at += '00'
            self.created_at = datetime.strptime(self.created_at, dt_format)


@dataclass
class GenreFilmWork:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_work_id: uuid.UUID = field(default_factory=uuid.uuid4)
    genre_id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = datetime.now()

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at += '00'
            self.created_at = datetime.strptime(self.created_at, dt_format)
