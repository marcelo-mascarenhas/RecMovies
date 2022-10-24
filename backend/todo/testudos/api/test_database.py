from todo.models import Movies
from mock_django.query import QuerySetMock
from todo.api import GetMovie, GetMostPopularMovies
import json
import pytest


def test_creation_of_movie():
  movie = Movies(
    title="Piratas do Caribe",
    language='pt',
    genres='Action',
  )
  
  assert str(movie.title) == "Piratas do Caribe"; assert str(movie.language) == 'pt'
  assert str(movie.genres) == 'Action'
  

@pytest.fixture
def insert_movies():
  
  movie1 = Movies(
    title="Inception",
    language='pt',
    genres='Science Fiction',
    popularity='100.0'
  )
  movie1.save()
  
  movie2 = Movies(
    title="Chihiro",
    language='jp',
    genres='Anime',
    popularity='120.0'
    
  )
  movie2.save()
  

@pytest.mark.django_db
def test_size_database(insert_movies):
  all_objects = Movies.objects.all()
  assert len(all_objects) == 2

@pytest.mark.django_db
def test_first_item_in_database(insert_movies):
  first_obj = Movies.objects.first()
  assert str(first_obj.title) == "Inception"

@pytest.mark.django_db
def test_popular_movies(insert_movies):

  get_popular_movies = GetMostPopularMovies()
  response = get_popular_movies.get(request="", number=2)
  data = response.data['data']
  all_keys = [data[0]['title'], data[1]['title']]
  
  assert all_keys == ['Chihiro', 'Inception']
  

# Mock example.
def test_get_movies(mocker):
  mock_first_movies = mocker.patch("todo.models.Movies.objects.filter")
  
  mock_first_movies.return_value =  [(Movies(
                                      title="Chihiro",
                                      language='jp',
                                      genres='Anime',
                                    ))]

  get_movie_obj = GetMovie()
 
  response = get_movie_obj.get(request="", movie_name="Chihiro", limit=1)

  data = response.data
  
  assert 'Chihiro' in data['data']



  
