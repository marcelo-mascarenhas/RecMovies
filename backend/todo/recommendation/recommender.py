from .recommendation_model import get_topic_matrix

def fromdf_todict(new_dataframe):
    """
    Creating dicts with columns required for wr
    """
    new_dict = new_dataframe[['popularity','vote_average','vote_count']].to_dict()
    
    return new_dict


def calculate_score(similarity, item_data, i, df_mean, min_votes):
    """
    Calculate the final score.
    
    """
    
    #(WR)=(v/(v+m))R+(m/(v+m))C      
    wr = ((item_data['vote_count'][i]/(item_data['vote_count'][i]+min_votes))\
      *item_data['vote_average'][i]+(min_votes/(item_data['vote_count'][i]+min_votes)))*df_mean

    final_score = 0.99*similarity + 0.01*wr 
    return final_score


def movie_recommender(data_id, new_dict):
    """
    Recomend top-10 items. 
    """
    position = new_dataframe[new_dataframe['id'] == id].index[0]
    content_vec = content_obj.item_matrix[position]
    dataframe_cpy = new_dataframe.copy()
    dataframe_cpy = dataframe_cpy.sort_values(by='vote_count', ascending=False)
    min_votes = dataframe_cpy['vote_count'][50]
    df_mean = new_dataframe['vote_average'].mean()
    final_dict = {}
    for i in range(len(new_dataframe)):
        if(i != position):
            target_vec = content_obj.item_matrix[i]
            similarity = content_obj.cossine(content_vec, target_vec)
            final_score = calculate_score(similarity, new_dict, i, df_mean, min_votes)
            final_dict[i] = final_score
    
    recom = dict(sorted(final_dict.items(), key=lambda item: item[1], reverse=True))
    final_recom = list(recom.keys())[:10]
    print(final_recom)
    recommendations = new_dataframe['id'].iloc[final_recom]
    
    return recommendations



def get_recommendations(movie_id, limit):
    matrix_topic = get_topic_matrix()
    
    print(matrix_topic)
    return 'ABALO'
