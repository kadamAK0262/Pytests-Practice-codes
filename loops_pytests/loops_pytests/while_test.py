
import pytest
from while_loop import calculate_factorial
from while_loop import generate_fibonacci_series

def test_calculate_factorial_zero():
    result = calculate_factorial(0)
    assert result == 1

def test_calculate_factorial_positive_number():
    result = calculate_factorial(5)
    assert result == 120

def test_calculate_factorial_large_number():
    result = calculate_factorial(10)
    assert result == 3628800



# test_fibonacci_series

def test_generate_fibonacci_series_zero_limit():
    result = generate_fibonacci_series(0)
    assert result == [0, 1]

def test_generate_fibonacci_series_positive_limit():
    result = generate_fibonacci_series(10)
    assert result == [0, 1, 1, 2, 3, 5, 8]

def test_generate_fibonacci_series_large_limit():
    result = generate_fibonacci_series(100)
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_generate_fibonacci_series_negative_limit():
    result = generate_fibonacci_series(-5)
    assert result == [0, 1]


