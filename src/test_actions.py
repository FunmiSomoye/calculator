import sys
#sys.path.append("../src")
sys.path.append("/Users/user/Documents/MyBasicCalculator/src/")
import pytest
from src import actions

cal = actions.Calculator()
root_cal = actions.Calculator(-10)

def test_add():
    assert cal.add([1, 2]) == 3.0
    assert cal.add([1, 2]) == 6.0
    assert cal.add([1]) == 7.0
    cal.clear_mem()
    assert cal.add([1]) == 1.0
    cal.clear_mem()
    assert cal.add([]) == 0.0
    cal.clear_mem()

def test_subtract():
    assert cal.subtract([5, 2]) == 3.0
    assert cal.subtract([4]) == -1.0
    assert cal.subtract([]) == -1.0
    cal.clear_mem()
    assert cal.subtract([5, 2, 3, 4]) == -4.0
    cal.clear_mem()
    assert cal.subtract([1]) == -1.0
    cal.clear_mem()
    assert cal.subtract([]) == 0.0
    cal.clear_mem()
  
def test_multiply():
    assert cal.multiply([1]) == 0.0
    assert cal.multiply([1, 2]) == 2.0
    assert cal.multiply([]) == 2.0
    cal.clear_mem()
    assert cal.multiply([]) == 0.0
    assert cal.multiply([1, 2]) == 2.0
    assert cal.multiply([4, 2]) == 16.0
    cal.clear_mem()
   
def test_divide():
    assert cal.divide(1) == 0.0
    assert cal.divide(1, 2) == 0.5
    assert cal.divide(2, 0) == 0.25
    assert cal.divide(4, 2) == 2.0
    assert cal.divide(1) == 2.0
    assert cal.divide(5, 2) == 2.5
    assert cal.divide() == 2.5
    cal.clear_mem()

def test_root():
    assert cal.root(2) == 0.0
    assert cal.root(1, 2) == 1.0
    assert cal.root(9, 2) == 3.0
    cal.clear_mem()
    assert cal.root(1) == 0.0
    



def test_value_error():
    with pytest.raises(ValueError):
        cal.add(['hello', 5]) 
        cal.add(['hello']) 
        cal.add([5, 'hello']) 
        cal.subtract(['hello', 5]) 
        cal.subtract(['hello']) 
        cal.subtract([5, 'hello']) 
        cal.multiply(['hello', 5]) 
        cal.multiply(['hello']) 
        cal.multiply([5, 'hello']) 
        cal.divide(['hello', 5]) 
        cal.divide(['hello']) 
        cal.divide([5, 'hello']) 
        cal.root(['hello', 5]) 
        cal.root(['hello']) 
        cal.root([5, 'hello']) 
        cal.root([-5, 2]) 
        root_cal.root([2]) 
