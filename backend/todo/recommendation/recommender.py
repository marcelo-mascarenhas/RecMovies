from .recommendation_model import get_parameters
import numpy as np
from ..models import Movies
import collections

def cossine(va, vb):
    #Cossine between normalized vector and crude item vector.
    cossine = np.dot(va,vb)/(np.linalg.norm(va)*np.linalg.norm(vb))

    return cossine


def calculate_wr(mtd, item, df_mean, min_votes):
    """
    Calculate the final score.
    
    """

    item_vote_count = np.array(mtd[item][1])
    item_vote_mean = np.array(mtd[item][0])
    item_minsum_count = item_vote_count + min_votes
    
    #(WR)=(v/(v+m))R+(m/(v+m))C  
    wr = ( (item_vote_count / (item_minsum_count) ) * item_vote_mean + (min_votes / (item_minsum_count) ) ) * df_mean

    return wr


def calculate_finalscore(similarity, wr):

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
            #tm = Movies.objects.get(id=item)

            target_vec = matrix_topic[int(item)]
            similarity = cossine(content_vec, target_vec)

            wr = calculate_wr(mtd, item, np.array(db_mean), np.array(min_votes))
            final_score = calculate_finalscore(np.array(similarity), wr)
            
            final_dict[int(item)] = float(final_score)

    final_dict = {k: v for k, v in sorted(final_dict.items(), key=lambda x: x[1])}
    final_recom = list(final_dict.keys())[-limit:]
    print(final_recom)
    return final_recom
