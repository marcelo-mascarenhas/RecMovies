from django.apps import AppConfig
from django.conf import settings
from .recommendation.recommendation_model import load_topic_matrix, load_parameters, load_mins


class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'
    
    def ready(self):
        # load_topic_matrix(settings.PATH_TO_MODEL)
        # load_parameters(settings.PATH_TO_ATT)
        # load_mins(settings.PATH_TO_MINS)
        pass