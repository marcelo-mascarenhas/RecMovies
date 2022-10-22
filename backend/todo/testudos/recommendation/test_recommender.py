from cmath import nan
import numpy as np
import pytest

from todo.recommendation.recommender import cossine

@pytest.mark.parametrize("first_array,second_array,expected_output",[
  (np.ones(3), np.ones(3), 1.0), 
         
  (np.array([1,0]), np.array([0,1]), 0.0),
        
  (np.array([0, 1]), np.array([0, -1]), -1.0),
        
  (np.array([0.5, 0.866]), np.array([1, 0]), 0.50)
  ])

def test_cossine_values(first_array, second_array, expected_output):
  result = cossine(first_array, second_array)
  assert pytest.approx(result, rel=1e-3) == expected_output

@pytest.mark.parametrize(
  "first_array,second_array,exception_type",
  [(np.zeros(3),np.zeros(5),ValueError),
   (None,None,TypeError)]
)

def test_cossine_with_different_dimension(first_array, second_array, exception_type):
  with pytest.raises(exception_type):
    cossine(first_array, second_array)
    
  


