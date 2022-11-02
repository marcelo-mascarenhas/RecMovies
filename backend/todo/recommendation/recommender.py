from attr import attributes
from .recommendation_model import RecommenderAttributes
import numpy as np
from ..models import Movies
import collections

def get_otherparams(matrix_topic, movie_id):
    all_ids = list(Movies.objects.values_list('id', flat=True))
    all_ids = np.asarray(all_ids)

    content_vec = matrix_topic[movie_id]

    final_dict = {}

    return all_ids, content_vec, final_dict


def cossine(va, vb):
    #Cossine between normalized vector and crude item vector.
    cossine = np.dot(va,vb)/(np.linalg.norm(va)*np.linalg.norm(vb))

    return cossine


def calculate_wr(mtd, item, df_mean, min_votes):
    """
    Calculate the final score.
    
    """

    item_vote_count = mtd[item][1]
    item_vote_mean = mtd[item][0]
    item_minsum_count = item_vote_count + min_votes
    
    #(WR)=(v/(v+m))R+(m/(v+m))C  
    wr = ( (item_vote_count / (item_minsum_count) ) * item_vote_mean + (min_votes / (item_minsum_count) ) ) * df_mean

    return wr


def calculate_finalscore(similarity, wr, item, final_dict):

    final_score = 0.99*similarity + 0.01*wr 
    
    final_dict[int(item)] = float(final_score)


def get_finalrecom(final_dict, limit):
    final_dict = {k: v for k, v in sorted(final_dict.items(), key=lambda x: x[1])}

    final_recom = list(final_dict.keys())[-limit:]

    return final_recom


def get_recommendations(movie_id, limit):
    attributes = RecommenderAttributes()

    matrix_topic, min_votes, db_mean, mtd  = attributes.get_parameters()

    all_ids, content_vec, final_dict = get_otherparams(matrix_topic, movie_id)
    
    for item in all_ids:
        if(item != movie_id):

            target_vec = matrix_topic[int(item)]
            similarity = cossine(content_vec, target_vec)

            wr = calculate_wr(mtd, item, db_mean, min_votes)
            
            calculate_finalscore(np.array(similarity), wr, item, final_dict)

    final_recom = get_finalrecom(final_dict, limit)
    
    return final_recom