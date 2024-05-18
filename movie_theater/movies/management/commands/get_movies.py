from django.core.management import BaseCommand
from django.utils.text import slugify
from django.conf import settings
import polars as pl
from datetime import datetime

from movies.models import Movie, Person, Genre


def to_movie(row: dict) -> Movie:
    actors = row.pop("actors", [])
    genres = row.pop("genres", [])
    image: str = row.pop("image", "")
    release_date = row.pop("release_date", None)
    row["release_date"] = datetime(release_date, 1, 1)
    actors_objs = []
    for actor in actors:
        actor, _ = Person.objects.get_or_create(name=actor, slug=slugify(actor))
        actors_objs.append(actor)

    genres_objs = []
    for genre in genres:
        genre, _ = Genre.objects.get_or_create(name=genre, slug=slugify(genre))
        genres_objs.append(genre)

    if image.startswith("/uploads/"):
        image = f"https://filmoflix.to{image}"

    movie = Movie.objects.create(
        **row,
        image=image,
        slug=slugify(row["title"]),
        genre=next(iter(genres_objs), None),
    )
    movie.actors.add(*actors_objs)


def movies_from_parquet():
    rows = pl.read_parquet(
        settings.BASE_DIR.parent / "movies.parquet",
        columns=(
            "title",
            "description",
            "url",
            "genres",
            "actors",
            "release_date",
            "image",
        ),
    ).iter_rows(named=True)
    list(map(to_movie, rows))


class Command(BaseCommand):
    def handle(self, *args, **options):
        movies_from_parquet()
        pass
