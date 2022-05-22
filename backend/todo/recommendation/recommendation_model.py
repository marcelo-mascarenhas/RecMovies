import pandas as pd



class Recommendation():
    def __init__(path, )
        topic_matrix = None


def load_topic_matrix(path):
    global topic_matrix
    df = pd.read_csv(path)
    topic_matrix = df.to_dict()

def get_topic_matrix():
    if topic_matrix is None:
        raise Exception('Topic Matrix não foi carregada.')
    else:
        return topic_matrix

