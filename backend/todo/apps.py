from django.apps import AppConfig
from django.conf import settings
from .recommendation.recommendation_model import RecommenderAttributes
import sys

class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'
    
    def ready(self):
        if 'unit' in sys.argv and 'pytest' in sys.modules:  # Check if running unit tests
            return  # Skip initialization during unit tests

        path_list = (settings.PATH_TO_MODEL, settings.PATH_TO_ATT, settings.PATH_TO_MINS)
        # Initializing singleton
        rec_obj_att = RecommenderAttributes(path_list)