from django.urls import path, include

from . import api

urlpatterns = [
    path(r"", api.Home.as_view(), name="Home"),
    path(r"api/movie/<movie_name>", api.GetMovie.as_view(), name="api-movies"),
    path(r"api/data/a1", api.ListUsers.as_view(), name="api-data-ScoreDistribution"),
]