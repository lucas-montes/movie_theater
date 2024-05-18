from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, Person


class MovieListView(ListView):
    paginate_by = 12
    model = Movie
    template_name = "movies.html"
    queryset = Movie.objects.order_by("-release_date")


class MovieDetailView(DetailView):
    model = Movie
    context_object_name = "movie"
    template_name = "detail.html"


class PersonListView(ListView):
    model = Person
    template_name = "actors.html"
    queryset = Person.objects.all()


def movies_by_actor(request, slug: str):
    queryset = Movie.objects.filter(actors__slug=slug)
    return render(request, "movies.html", {"object_list": queryset})


def movies_by_genre(request, slug: str):
    queryset = Movie.objects.filter(genre__slug=slug)
    return render(request, "movies.html", {"object_list": queryset})
