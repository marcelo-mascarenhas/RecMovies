#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
   Imports needed
"""
import pandas as pd
import sqlite3
import numpy as np
import gensim
from nltk.corpus import stopwords
import spacy


# In[2]:


class TextProcessor():
  """
    Class responsible for treating the dataset and training the LDA model.
  """

  def tokenize(self, df_overviews):
      """
      Tokenize the dataset. Return a list of str list, where the latter represent the list of words of each overview.
      
      """
      return [gensim.utils.simple_preprocess(overview, deacc=True) for overview in df_overviews]
  
  def construct_bigrams(self, tokenized_overview):
      """
      Receives a list of str lists.
      
      Construct bigrams(two words terms), conservating the meaning of some sentences.
      Ex: The bigram 'United States' is much more meaningful than the two unigrams 'United' and 'States'.
      The same follows for inumerous terms.
      
      Returns the tokenized overview with bigrams.
      """
                    #A bigram should appear at least 10 times in the dataset to be considered.
      bg = gensim.models.Phrases(tokenized_overview, min_count=5, threshold=10) 
                                                        #Higher threshold means less bigrams.
      bg_mod = gensim.models.phrases.Phraser(bg)

      return [bg_mod[overview] for overview in tokenized_overview]
  
  def remove_english_stopwords(self, all_tokenized_overviews, additional_stopwords = []):
      """
      Remove stopwords from dataset.
      
      """

      english_stopwords = stopwords.words("english") + additional_stopwords
      return [[word for word in overview if word not in english_stopwords] for overview in all_tokenized_overviews]
  
  def lemmatization(self, texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
      """https://spacy.io/api/annotation"""        
      
      nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])

      texts_out = []
      for sent in texts:
          doc = nlp(" ".join(sent)) 
          texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
      return texts_out

  def text_process(self,
                    doc_set,
                    extra_stop_words=[]):
      """
      
      Tokenize, remove stopwords, generate bigrams and lemmatize the dataset.
      Returns the filtered dataset
      
      Parameters
      -----------
      doc_set: List of list of documents that will be treated.
      extra_stop_words: Additional stopwords that will be used together with nltk.corpus stopwords.
      """
      # generate a list of tokenized plots.
      tokenized_overview = self.tokenize(doc_set)
      # remove stopwords
      ens = self.remove_english_stopwords(tokenized_overview, extra_stop_words)
      # generate bigrams.
      bigram_tokenized = self.construct_bigrams(ens)
      # lemmatize dataset.
      treated_dataset = self.lemmatization(bigram_tokenized)
      
      return treated_dataset
      
      

  def create_corpus(self, texts):
      # turn our tokenized documents into an id <-> term dictionary
      dictionary = gensim.corpora.Dictionary(texts)
      # Filtering words that appears in less than 1 and more than 80% of documents.
      dictionary.filter_extremes(no_below=2, no_above=0.80)
      dictionary.compactify()

      # convert tokenized documents into a document-term matrix
      corpus = [dictionary.doc2bow(text) for text in texts]

      return (corpus, dictionary)
  
  def generate_lda(self, corpus, dictionary, num_topics, epochs=200, passes=300, chunksize=90000):
      """
      Generate LDA model and returns it.
      
      Parameters
      -----------
      corpus: tokenized documents in a document-term matrix. (Use create_corpus to generate it)
      dictionary: auxiliar structure 
      num_topics : number of topics that will be created
     
      epochs: number of training iterations
      
      passes: number of times that each document will be utilized in a specific iteraiton
      
      chunksize: number of documents that will be considered in an iteration.
      
      Return
      -------
      
      Trained LDA model.
      
      """
      model = gensim.models.ldamodel.LdaModel(corpus=corpus, 
                                              num_topics=num_topics, 
                                              iterations=epochs,
                                              passes=passes,
                                              chunksize=chunksize,
                                              id2word=dictionary,
                                              alpha="auto")

      return model


# In[3]:


class LDAContentBasedRecommender():
  """
  Content Based recommender 

  """
  def __init__(self, model, matrix_document_topic, item_dictionary, default_k = 5, sim_method= None):
    """
    Parameters
    -----------
    model -> LDA or HDP model.
    
    matrix_document_topic -> Matrix that stores the distribution of each topic in the documents.
    It can be obtained by model[corpus], if the model was calculated using gensim library. 

    item_dictionary -> Dictionary that maps the id with its position in the dataset
    (must correspond with the corpus used to train the LDA model.)
    
    Optional
    ---------
    
    default_k => Number of the closest items that will be consireded in the KNN evaluation.
    
    sim_method (functional type) => Similarity method. 
    If nothing is passed, then cossine will be used.
    
    """
    self.model = model
    
    self.corpus_lda = matrix_document_topic
    
    self.len = model.num_topics
    
    #Document distribution over topics.
    self.item_matrix = self.__doc_x_topics() 
    
    # ItemID <-> Position_in_the_matrix dictionary
    self.item_dic = item_dictionary 
    
    self.k = default_k 
    
    self.sim_method = sim_method if sim_method != None else self.cossine
    
  def __doc_x_topics(self):    
    """
    Generate the documents x topics matrix that will be used to calculate the scores.
    """
    
    item_matrix = gensim.similarities.MatrixSimilarity(self.corpus_lda).index
    
    return item_matrix
  

  def cossine(self, va, vb):
    #Cossine between normalized vector and crude item vector.
    cossine = np.dot(va,vb)/(np.linalg.norm(va)*np.linalg.norm(vb))
    
    return cossine   
    
    
  def getScore(self, all_evaluations, item_vector):
      """
        Predict the score of a target item utilizing the top K most similar components based on
        the user's previous rated items.
        
        The calculation is made by adding the product of each one of the top K scores given by an user
        and the similarity between the target item and the rated item vector, using the similarity method 
        passed in the method.
        
        Parameters
        -----------
        all_evaluation (dataframe) => dataframe that contains all the user's rated items.
        
        item_vector (np.array) => target item vector 

        Returns
        --------
        score (int) => Predicted score of the target item.
      
      """
      
      score = 0
      
      #Get the similarity score with the chosen method between the target item and all the other
      #items that a specific user consumed.
      all_evaluations['Similarity'] = all_evaluations.apply(lambda x: 
        self.sim_method(item_vector,  self.item_matrix[self.item_dic[x['ItemId']], :]), 
        axis=1)
      
      #Sort the similarity in decreasing order.
      all_evaluations.sort_values(by='Similarity', ascending=False, inplace=True)
      
      main_items = None
      
      #Get the top K items if the number of elements in the dataset is greater than the K. Else take all elements. 
      if len(all_evaluations) > self.k:
        main_items = all_evaluations[0:self.k].to_numpy()
      else:
        main_items = all_evaluations.to_numpy()
      
      #The score of the item will be the sum of the ratings times the similarity of the predicted item and the top k consumed item.
      for _, rating, similarity in main_items:
        score += similarity*rating
      
      #Normalize the score
      score /= len(main_items)   
            
      return score


# In[4]:


def treat_df(dataset):
    dataset = dataset.drop(['poster_path','release_date','language'], axis=1)
    
    return dataset


def lda_training(dataset, number_of_topics_lda):
   #Selecting columns to train LDA.
   target_dataset = dataset[['title', 'genres']].copy()
  
   #Removing any N/A, NaN or None from these columns.
   target_dataset = target_dataset.apply(lambda row: " ".join(row.values.astype(str))      .replace("N/A", "").replace("NaN", "").replace("None", ""), axis=1)

   tto = TextProcessor()

   #Processing the text.
   tokenized = tto.text_process(target_dataset)
  
   (corpus, dictionary) = tto.create_corpus(tokenized)

   #Generates LDA Model.
   lda_model = tto.generate_lda(corpus, dictionary, number_of_topics_lda)
  
   #Matrix that represents the distribution of topics from the documents.
   lda_matrix = lda_model[corpus]
  
   return (lda_model, lda_matrix)


def create_content_obj(content_dataframe):
  number_of_topics = 50
  
  lda_model, lda_matrix = lda_training(content_dataframe, number_of_topics)
  
  #Item dictionary.
  item_dictionary = {v: k for k,v in enumerate(content_dataframe['id'])}
  
  #Creating content Object
  content_obj = LDAContentBasedRecommender(lda_model, lda_matrix, item_dictionary)  

  return content_obj

#Open dataframes
dat = sqlite3.connect('/Users/matheuspradomiranda/TP-Eng-Soft1/backend/database/db.sqlite3')
dataframe = pd.read_sql_query('SELECT * FROM todo_movies',dat)

new_dataframe = treat_df(dataframe)

content_obj = create_content_obj(new_dataframe)


# In[5]:


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
    wr = ((item_data['vote_count'][i]/(item_data['vote_count'][i]+min_votes))      *item_data['vote_average'][i]+(min_votes/(item_data['vote_count'][i]+min_votes)))*df_mean

    final_score = 0.99*similarity + 0.01*wr 
    return final_score


def movie_recommender(title, new_dict, position, content_vec):
    """
    Recomend top-10 items.
    """
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
    recommendations = new_dataframe['title'].iloc[final_recom]
    
    return recommendations


# In[6]:


# position = new_dataframe[new_dataframe['title'] == "The Lord of the Rings: The Fellowship of the Ring"].index[0]
# content_vec = content_obj.item_matrix[position]


# In[8]:


def id_dict(new_dataframe, topic_vec):
   new_dict = {}
   for i in range(len(topic_vec)):
        new_dict[new_dataframe['id'].iloc[i]] = topic_vec[i]
    
   return new_dict


# In[9]:


def calc_idlist(new_dataframe):
    id_list = []
    for i in range(len(new_dataframe)):
        id_list.append(new_dataframe['id'].iloc[i])
    return id_list


# In[10]:


def dict_fromdf(df):
    new_dict = {}
    for key, value in df.iteritems():     
        l=[]
        for x in value:
            l.append(x)
        new_dict[key] = tuple(l)
    del new_dict['Unnamed: 0']
    return new_dict


# In[47]:


def votes_dict(df):
    new_dict = {}
    for i in range(len(new_dataframe)):
        new_dict[new_dataframe['id'].iloc[i]] = new_dataframe['vote_average'].iloc[i], new_dataframe['vote_count'].iloc[i]
    return new_dict


# In[43]:


def fromdfavgvote_todict(df_teste):
    dict_t = {}
    for i in range(len(df_teste)):
        dict_t[df_teste['Unnamed: 0'].iloc[i]] = df_teste['0'].iloc[i], df_teste['1'].iloc[i]
    return dict_t

dict_tal = fromdfavgvote_todict(df_teste)

