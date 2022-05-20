from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.forms.models import model_to_dict
from .serializers import TodoSerializer
from .models import Movies
from unidecode import unidecode
import json


class Home(APIView):
  def get(self, request):
    return Response('Welcome to the ABALO.')


class GetMovie(APIView):
  authentication_classes = []
  permission_classes = []
  def get(self, request, movie_name):
    count_dict = {}
    movie_name = unidecode(movie_name)
    o1 = Movies.objects.filter(title__contains=movie_name)
    
    count_dict['data'] = {}
    
    for star in o1.iterator():
      count_dict['data'][star.title] = model_to_dict(star)
    
    return Response(count_dict)  



class ListUsers(APIView):
  authentication_classes = []
  permission_classes = []

  def get(self, request):
    return Response({'ab': 3})
