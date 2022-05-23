from django.shortcuts import render

import operator
from functools import reduce

from .serializers import TodoSerializer
from .models import Movies

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

import json
from unidecode import unidecode
from .utils import getMovieDictionary
from .crawlers.remove import remove_adult
from .recommendation.recommender import get_recommendations


class Home(APIView):
  def get(self, request):
    return Response('Welcome to the ABALO.')


class GetMostPopularMovies(APIView):
  """
  Chamada da API responsável por retonar uma quantidade passada
  de filmes mais populares.
  """
  def get(self, request, number):
    """
    
    Parâmetros
    ----------

    (INT) number: Threshold que define quantos filmes 'mais populares' serão retornados
    na chamada.
    
    """
    count_dict = {}
    o1 = Movies.objects.all().order_by('-popularity')[:number]
    #Movies.objects.filter(id=ID_DO_FILME)
    #aggregateMovies.object.all()
    final_response = getMovieDictionary(o1, title_as_key=False)
    
    return Response(final_response)  

class GetMovie(APIView):
  """
  Chamada da API que recuperam os filmes buscados.
  """
  
  authentication_classes = []
  permission_classes = []
  def get(self, request, movie_name, limit):
    """
    
    Parâmetros
    ----------

    (STR) movie_name

    (INT) limit : Delimitador que define até quantos filmes podem ser retornados, caso exista
    mais de um filme com mesmo nome no database.
    
    """
    
    
    movie_name = unidecode(movie_name)
    o1 = Movies.objects.filter(title__contains=movie_name)[:limit]
    
    final_response = getMovieDictionary(o1)
    
    return Response(final_response)  



class GetRecommendation(APIView):
  authentication_classes = []
  permission_classes = []

  def get(self, request, movie_id, limit):
    try:
      recommendation_list = get_recommendations(movie_id, limit)
      o1 = Movies.objects.filter(id__in=recommendation_list)
      final_response = getMovieDictionary(o1)
    
    except Exception as e:
      final_response = {}

    return Response(final_response)
    