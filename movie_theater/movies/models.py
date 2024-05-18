from django.db import models


# Un Model est la representation d'une table dans la base de données
class Person(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.URLField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField()
    url = models.URLField()
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    actors = models.ManyToManyField(
        Person,
        blank=True,
    )
    release_date = models.DateField()
    image = models.URLField()

    def __str__(self):
        return self.title
