from django.apps import AppConfig
from django.conf import settings
from .recommendation.recommendation_model import RecommenderAttributes


class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'
    
    def ready(self):
        path_list = (settings.PATH_TO_MODEL, settings.PATH_TO_ATT, settings.PATH_TO_MINS)
        #Initializing singleton;
        rec_obj_att = RecommenderAttributes(path_list)
        
        # load_topic_matrix(settings.PATH_TO_MODEL)
        # load_parameters(settings.PATH_TO_ATT)
        # load_mins(settings.PATH_TO_MINS)