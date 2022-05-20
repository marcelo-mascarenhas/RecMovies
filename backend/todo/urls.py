from django.urls import path, include

from . import api

urlpatterns = [
    path(r"", api.Home.as_view(), name="Home"),
    path(r"api/data/a1", api.ListUsers.as_view(), name="api-data-hist1"),
    path(r"api/data/a2", api.GetScores.as_view(), name="api-data-ScoreDistribution"),
]