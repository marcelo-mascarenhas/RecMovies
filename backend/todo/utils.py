from .models import Movies
from django.forms.models import model_to_dict



def getMovieDictionary(database_object):
    movies = {}
    movies['data'] = {}
    
    for star in database_object.iterator():
      movies['data'][star.title] = model_to_dict(star)
    
    return movies    