from .recommendation_model import get_parameters
import numpy as np
from ..models import Movies
import collections

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
    matrix_topic, min_votes, db_mean, mtd  = get_parameters()
    all_ids = list(Movies.objects.values_list('id', flat=True))
    all_ids = np.asarray(all_ids)
    content_vec = matrix_topic[movie_id]

    final_dict = {}
    
    for item in all_ids:
        if(item != movie_id):
            print(item)
            #tm = Movies.objects.get(id=item)

            target_vec = matrix_topic[int(item)]

            similarity = cossine(content_vec, target_vec)
            final_score = calculate_score(np.array(similarity), np.array(mtd[item][1]),np.array(mtd[item][0]), np.array(db_mean), np.array(min_votes))
            final_dict[int(item)] = float(final_score)

    final_dict = {k: v for k, v in sorted(final_dict.items(), key=lambda x: x[1])}
    final_recom = list(final_dict.keys())[-limit:]
    print(final_recom)
    return final_recom
