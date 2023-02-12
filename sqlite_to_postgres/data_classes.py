import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone

dt_format = '%Y-%m-%d %H:%M:%S.%f+00'


@dataclass
class FilmWork:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    title: str = ''
    description: str = ''
    creation_date: str = ''
    file_path: str = ''
    rating: float = field(default=0.0)
    type: str = ''
    created_at: str = ''
    updated_at: str = ''

    def __post_init__(self):
        if not isinstance(self.created_at, datetime):
            self.created_at = datetime.strptime(self.created_at, dt_format)
            self.created_at.astimezone(timezone.utc)
        if not isinstance(self.updated_at, datetime):
            self.updated_at = datetime.strptime(self.updated_at, dt_format)
            self.updated_at.timezone(timezone.utc)


@dataclass
class Person:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    full_name: str = field(default='')
    created_at: str = ''
    updated_at: str = ''

    def __post_init__(self):
        if not isinstance(self.created_at, datetime):
            self.created_at = datetime.strptime(self.created_at, dt_format)
            self.created_at.astimezone(timezone.utc)
        else:
            self.created_at.astimezone(timezone.utc)
        if not isinstance(self.updated_at, datetime):
            self.updated_at = datetime.strptime(self.updated_at, dt_format)
            self.updated_at.astimezone(timezone.utc)


@dataclass
class Genre:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    name: str = ''
    description: str = ''
    created_at: str = ''
    updated_at: str = ''

    def __post_init__(self):
        if not isinstance(self.created_at, datetime):
            self.created_at = datetime.strptime(self.created_at, dt_format)
            self.created_at.astimezone(timezone.utc)
        if not isinstance(self.updated_at, datetime):
            self.updated_at = datetime.strptime(self.updated_at, dt_format)
            self.updated_at.astimezone(timezone.utc)


@dataclass
class PersonFilmWork:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_work_id: uuid.UUID = field(default_factory=uuid.uuid4)
    person_id: uuid.UUID = field(default_factory=uuid.uuid4)
    role: str = ''
    created_at: str = ''

    def __post_init__(self):
        if not isinstance(self.created_at, datetime):
            self.created_at = datetime.strptime(self.created_at, dt_format)
            self.created_at.astimezone(timezone.utc)


@dataclass
class GenreFilmWork:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_work_id: uuid.UUID = field(default_factory=uuid.uuid4)
    genre_id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: str = ''

    def __post_init__(self):
        if not isinstance(self.created_at, datetime):
            self.created_at = datetime.strptime(self.created_at, dt_format)
            self.created_at.astimezone(timezone.utc)
