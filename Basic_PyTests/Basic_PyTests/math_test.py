import math_func
import pytest

# command for run method : pytest -v -k "method name"
# command for show failure pytest -v -x    or  pytest -v --maxfail="any number we want"
# command for ignore stack trace  pytest -v -x --tb=no 
# command for show the print statements : pytest -v -s
# @pytest.mark... Marker for group testing. command : pytest -v -m markerName
# @pytest.mark.skip(reason =" Any reason") : It will skip the method.

@pytest.mark.number    
def test_add():
    assert math_func.add(7,3)==10
    assert math_func.add(7)== 9

@pytest.mark.number
def test_product():
    assert math_func.product(5,5) == 25
    assert math_func.product(6) == 12

@pytest.mark.string
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == "Hello World"
    assert type(result) is str
    assert 'Heldlo' not in result

@pytest.mark.string
def test_product_strings():
    assert math_func.product('Hello ', 3)== 'Hello Hello Hello '

    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result

@pytest.mark.number
def test_sub():
    result = math_func.sub(8, 4)
    assert result == 4
    assert result < 6

# Parametrize testing example 
@pytest.mark.number
@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 3, 4),
                             (8, 4, 4),
                             (10.5, 5.5, 5)
                         ])
def test_sub_parametrize(num1, num2, result):
    assert math_func.sub(num1, num2) == result

