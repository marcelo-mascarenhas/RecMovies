import pandas as pd
import numpy as np

# class RecommenderAttributes():
#     def __init__(self):
#         self.topic_matrix = None
        
#         self.min_votes = 0
        
#         self.db_mean = 0
        
#         self.mtd = None
    
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(RecommenderAttributes, cls).__new__(cls)
        
#         return cls.instance    
    
    
#     def set_parameters(self):
        
    
    
#     def get_parameters(self):
#         return np.array(self.topic_matrix), np.array(self.min_votes), np.array(self.db_mean), mtd
    

def dict_fromdf(df):
    dicted_convert = {}
    first_iteration = True
    for key, value in df.iteritems():
        
        if not first_iteration:
            value_list = []
            
            for x in value:
                value_list.append(x)    
            
            dicted_convert[int(key)] = np.array(value_list)
        
        first_iteration = False
    
    return dicted_convert

topic_matrix = None
min_votes = 0
db_mean = 0
mtd = None




def load_topic_matrix(path):
    global topic_matrix
    df = pd.read_csv(path)
    topic_matrix = dict_fromdf(df)

def load_parameters(path):
    global min_votes, db_mean
    df = pd.read_csv(path)
    min_votes = df['min_votes']
    db_mean = df['mean']


def load_mins(path):
    global mtd
    df = pd.read_csv(path)

    mtd = {}
    for i in range(len(df)):
        mtd[int(df['Unnamed: 0'].iloc[i])] = float(df['0'].iloc[i]), float(df['1'].iloc[i])
    

def get_parameters():
    if topic_matrix is None:
        raise Exception('Topic Matrix não foi carregada.')
    else:
        return topic_matrix, min_votes, db_mean, mtd

def get_recommendations(movie_id, limit):
    topic_matrix = get_topic_matrix()
    