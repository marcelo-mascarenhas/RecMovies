from django.urls import path, include

from . import api

urlpatterns = [
    path(r"", api.Home.as_view(), name="Home"),
    path(r"api/movie/<movie_name>/<int:limit>", api.GetMovie.as_view(), name="api-movie"),
    path(r"api/popular_movies/<int:number>", api.GetMostPopularMovies.as_view(), name="api-most_pop_movies"),
    path(r"api/get_movie_rec/<movie_name>/<int:limit>", api.GetRecommendation.as_view(), name="api-recommendations"),
]