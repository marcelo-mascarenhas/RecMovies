
from unicodedata import name
from requests import patch
import os
import sys

# BASE_PATH = os.path.dirname(os.path.abspath(__file__)).rsplit('/', 2)[0]
# sys.path.insert(0, BASE_PATH)
# from models import Movies

from todo.models import Movies
import pytest


# Teste de integração com os objetos. 
@pytest.mark.django_db
def test_creation_of_movie():
  movie = Movies(
    title="Piratas do Caribe",
    language='pt',
    genres='Action'
  )
  
  assert str(movie.title) == "Piratas do Caribe"
  assert str(movie.language) == 'pt'
  assert str(movie.genres) == 'Action'
  
  
