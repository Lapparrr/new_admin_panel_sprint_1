from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import Genre, Filmwork, GenreFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork

@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline,)
        # Отображение полей в списк