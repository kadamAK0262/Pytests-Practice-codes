# test_prime_number.py
from prime_no import is_prime

def test_is_prime_negative_number():
    result = is_prime(-5)
    assert not result

def test_is_prime_zero():
    result = is_prime(0)
    assert not result

def test_is_prime_one():
    result = is_prime(1)
    assert not result

def test_is_prime_small_prime_number():
    result = is_prime(7)
    assert result

def test_is_prime_large_prime_number():
    result = is_prime(97)
    assert result

def test_is_prime_non_prime_number():
    result = is_prime(15)
    assert not result

def test_is_prime_negative_prime_number():
    result = is_prime(-2)
    assert not result
