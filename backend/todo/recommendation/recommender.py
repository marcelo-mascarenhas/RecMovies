from .recommendation_model import get_parameters
import numpy as np
from ..models import Movies

def cossine(va, vb):
    #Cossine between normalized vector and crude item vector.
    cossine = np.dot(va,vb)/(np.linalg.norm(va)*np.linalg.norm(vb))

    return cossine


def calculate_score(similarity, item_vote_count, item_vote_mean, df_mean, min_votes):
    """
    Calculate the final score.
    
    """
    
    #(WR)=(v/(v+m))R+(m/(v+m))C      
    wr = ((item_vote_count/(item_vote_count+min_votes))\
      *item_vote_mean+(min_votes/(item_vote_count+min_votes)))*df_mean

    final_score = 0.99*similarity + 0.01*wr 
    return final_score



def get_recommendations(movie_id, limit):
    matrix_topic, min_votes, db_mean  = get_parameters()
    all_ids = Movies.objects.values_list('id', flat=True)
    content_vec = matrix_topic[movie_id]

    final_dict = {}
    
    for item in all_ids:
        if(item != movie_id):
            print(item)
            #tm = Movies.objects.get(id=item)

            target_vec = matrix_topic[int(item)]

            similarity = cossine(content_vec, target_vec)
            final_score = calculate_score(similarity, 1, 1, db_mean, min_votes)
            final_dict[int(item)] = float(final_score)
    
    recom = sorted(final_dict.items(), key=lambda item: item[1], reverse=True)
    final_recom = list(final_dict.keys())[:limit]
    print(final_recom)
    return final_recom
