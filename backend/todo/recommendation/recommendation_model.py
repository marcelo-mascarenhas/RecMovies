import pandas as pd
import numpy as np

topic_matrix = None
min_votes = 0
db_mean = 0
mtd = None

def dict_fromdf(df):
    new_dict = {}
    i = 0
    for key, value in df.iteritems():
         if i == 0:
            i+=1
            continue
            
         l=[]
         for x in value:
             l.append(x)
         new_dict[int(key)] = np.array(l)
    
    return new_dict


def load_topic_matrix(path):
    global topic_matrix
    df = pd.read_csv(path)
    topic_matrix = dict_fromdf(df)

def load_parameters(path):
    global min_votes, db_mean
    df = pd.read_csv(path)
    min_votes = df['min_votes']
    db_mean = df['mean']

def get_parameters():
    if topic_matrix is None:
        raise Exception('Topic Matrix não foi carregada.')
    else:
        return topic_matrix, min_votes, db_mean

def get_recommendations(movie_id, limit):
    topic_matrix = get_topic_matrix()
    