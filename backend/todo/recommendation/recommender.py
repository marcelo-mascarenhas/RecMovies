from .recommendation_model import get_topic_matrix
from django.db.models import Avg




def get_recommendations(movie_id, limit):
    matrix_topic = get_topic_matrix()
    print(matrix_topic)
    return 'ABALO'