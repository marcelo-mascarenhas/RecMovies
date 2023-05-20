from cmath import nan
import numpy as np
import pytest

from todo.recommendation.recommender import cossine, calculate_wr, calculate_finalscore

@pytest.mark.unit
class TestRecommendation():
    

  @pytest.mark.parametrize("first_array,second_array,expected_output",[
    (np.ones(3), np.ones(3), 1.0), 
          
    (np.array([1,0]), np.array([0,1]), 0.0),
          
    (np.array([0, 1]), np.array([0, -1]), -1.0),
          
    (np.array([0.5, 0.866]), np.array([1, 0]), 0.50)
    ])

  def test_cossine_values(self, first_array, second_array, expected_output):
    result = cossine(first_array, second_array)
    assert pytest.approx(result, rel=1e-3) == expected_output

  @pytest.mark.parametrize(
    "first_array,second_array,exception_type",
    [(np.zeros(3),np.zeros(5),ValueError),
    (None,None,TypeError)]
  )

  def test_cossine_with_different_dimension(self, first_array, second_array, exception_type):
    with pytest.raises(exception_type):
      cossine(first_array, second_array)

  @pytest.mark.parametrize("weighted_scores,similarities,answer",[
    (-0.0000000000001, 1.0000000000001, 0),
    (1, 1, 1),
    (0, 0, 0)
  ])

  def test_calculate_testscores_edge_cases(self, weighted_scores, similarities, answer):
    item_recom = {}; item = 2;
    calculate_finalscore(similarities, weighted_scores, item, item_recom)
    assert item_recom[item] == answer
    

  def test_calculate_wr_without_zero(self):
    data_without_zero = {"title": "Wonderland", "language": "en", 
    "genres":"Fantasy", 
    "overview": "Wonderland is a movie that shows the adventures of a girl in a fantasy world", 
    "popularity":100.0, 
    "poster_path": "./img/poster_wonderland", 
    "release_date": "2010-01-01", 
    "vote": [5.6, 10]}
    result = calculate_wr(data_without_zero, 'vote', 6.4, 4)
    assert round(result, 3) == 27.429
    
  def test_calculate_wr_with_zero(self):
    data_without_zero = {"title": "The Promise Land", "language": "en", 
    "genres":"Fantasy, Adventure, Monsters, Crime", 
    "overview": "The movie tells a story about three fairy children in a magical land.", 
    "popularity": 1337.0, 
    "poster_path": "./img/poster_tpl", 
    "release_date": "2011-11-11", 
    "vote": [5.6, 0]}
    with pytest.raises(ZeroDivisionError):
      calculate_wr(data_without_zero, 'vote', 6.4, 0)
    
    


