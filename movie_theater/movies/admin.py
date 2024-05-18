from django.contrib import admin

from .models import Person, Movie, Genre


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug", "image"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "description",
        "slug",
        "url",
        "genre",
        "release_date",
        "image",
    ]
    list_editable = [
        "title",
        "description",
        "slug",
        "url",
        "genre",
        "release_date",
        "image",
    ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
