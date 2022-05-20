from django.shortcuts import render

from .serializers import TodoSerializer
from .models import Movies

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

import json
from unidecode import unidecode
from .utils import getMovieDictionary

class Home(APIView):
  def get(self, request):
    return Response('Welcome to the ABALO.')



class GetMostPopularMovies(APIView):
  """
  Chamada da API responsável por retonar os X filmes mais populares.
  """
  def get(self, request, number):
    count_dict = {}
    o1 = Movies.objects.all().order_by('-popularity')[:number]
    final_response = getMovieDictionary(o1)
    
    return Response(final_response)  

class GetMovie(APIView):
  authentication_classes = []
  permission_classes = []
  def get(self, request, movie_name):
    movies = {}
    movie_name = unidecode(movie_name)
    o1 = Movies.objects.filter(title__contains=movie_name)
    
    final_response = getMovieDictionary(o1)
    
    return Response(final_response)  



class ListUsers(APIView):
  authentication_classes = []
  permission_classes = []

  def get(self, request):
    return Response({'ab': 3})
