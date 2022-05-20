from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .serializers import TodoSerializer
from .models import Movies


class Home(APIView):
  def get(self, request):
    return Response('Welcome to the ABALO.')


class GetScores(APIView):
  authentication_classes = []
  permission_classes = []
  
  def get(self, request):

    return Response({'ab': 3})


class ListUsers(APIView):
  authentication_classes = []
  permission_classes = []

  def get(self, request):
    return Response({'ab': 3})
