from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import Avg, Count, Max, Min, Sum, Value, F


def show_all_movie(request):
    movies = Movie.objects.all()
    agg = movies.aggregate(Sum('budget'), Max('budget'), Count('rating'))
    return render(request, 'movie_app/all_movies.html', context={
        'movies': movies,
        'agg': agg
    })


def show_one_movie(request, slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', context={'movie': movie})
