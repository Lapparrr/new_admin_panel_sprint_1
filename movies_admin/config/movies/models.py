from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        # Этот параметр указывает Django, что этот класс не является представлением таблицы
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):

    # Первым аргументом обычно идёт человекочитаемое название поля
    name = models.CharField('name', max_length=255)
    # blank=True делает поле необязательным для заполнения.
    description = models.TextField('description', blank=True)

    # auto_now_add автоматически выставит дату создания записи

    def __str__(self):
        return self.name

    class Meta:
        # Ваши таблицы находятся в нестандартной схеме. Это нужно указать в классе модели
        db_table = "content\".\"genre"
        # Следующие два поля отвечают за название модели в интерфейсе
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Filmwork(UUIDMixin, TimeStampedMixin):
    TYPE_CHOICES = [('MOV', 'movie'), ('TVS', 'tv_show')]
    title = models.CharField('title', max_length=255)

    description = models.TextField('description', blank=True)
    rating = models.FloatField('Rating', blank=True,
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(100)])
    type = models.CharField("type", choices=TYPE_CHOICES, blank=True, max_length=3)
    genres = models.ManyToManyField(Genre, through='GenreFilmwork')

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'Кино'
        verbose_name_plural = 'Кино'


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
