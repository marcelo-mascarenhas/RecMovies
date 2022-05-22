from .recommendation_model import get_topic_matrix




def get_recommendations(movie_id, limit):
    matrix_topic = get_topic_matrix()
    print(matrix_topic)
    return 'ABALO'