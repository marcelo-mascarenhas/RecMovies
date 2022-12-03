import pandas as pd
import numpy as np
import threading

class ThreadSafeSingleton(type):    
    _instances = {}
    _singleton_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._singleton_lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(ThreadSafeSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class RecommenderAttributes(metaclass=ThreadSafeSingleton):
    
    def __init__(self, *args, **kwargs):
        
        if len(args) != 1:
            raise Exception('Path_list não passada para a inicialização da classe.')
        
        path_list = args[0];
        
        self.topic_matrix = None
        
        self.min_votes = 0; self.db_mean = 0; self.mtd = None;
        
        self.load_all_parameters(path_list)
    
    def __load_matrix(self, matrix_path):
        df = pd.read_csv(matrix_path)
        self.topic_matrix = self.__dict_fromdf(df)
        
        
    def __load_parameters(self, parameter_path):
        df = pd.read_csv(parameter_path)
        self.min_votes = np.array(df['min_votes'])
        self.db_mean = np.array(df['mean'])
    
    def __load_mins(self, min_path):
        df = pd.read_csv(min_path)

        self.mtd = {}
        
        for i in range(len(df)):
            
            current_item = int(df['Unnamed: 0'].iloc[i]);
            
            first_position = np.array(df['0'].iloc[i]); second_position = np.array(df['1'].iloc[i]);
            
            self.mtd[current_item] = (first_position, second_position)
            
    def load_all_parameters(self, path_list):
        """
            path_list: tuple of paths containing the paths of all recommender parameters, such that the
            first element has the path to the matrix, the second to the parameters and the third to the mins
        
        """
        mat_path, par_path, min_path = path_list
        self.__load_matrix(mat_path); self.__load_parameters(par_path);
        self.__load_mins(min_path);
    
    
    
    def get_parameters(self):
        return self.topic_matrix, self.min_votes, self.db_mean, self.mtd
    
    
    def __dict_fromdf(self, df):
        dicted_convert = {}
        first_iteration = True
        
        for key, value in df.items():
            
            if not first_iteration:
                value_list = []
                
                for x in value:
                    value_list.append(x)    
                
                dicted_convert[int(key)] = np.array(value_list)
            
            first_iteration = False
        
        return dicted_convert