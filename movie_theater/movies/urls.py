from django.urls import path

from .views import (
    MovieListView,
    MovieDetailView,
    PersonListView,
    movies_by_actor,
    movies_by_genre,
)

urlpatterns = [
    path("", MovieListView.as_view(), name="movies"),
    path("actors/", PersonListView.as_view(), name="actors"),
    path("movies/<slug>/", MovieDetailView.as_view(), name="movie"),
    path("actors/<slug>/", movies_by_actor, name="actor"),
    path("genres/<slug>/", movies_by_genre, name="genre"),
]
