
import pytest
from forloop import sum_elements
from forloop import find_vowels_and_consonants

def test_sum_elements_empty_list():
    result = sum_elements([])
    assert result == 0

def test_sum_elements_positive_numbers():
    result = sum_elements([1, 2, 3, 4, 5])
    assert result == 15

def test_sum_elements_mixed_numbers():
    result = sum_elements([-1, 2, -3, 4, -5])
    assert result == -3



# test_vowels_consonants


def test_find_vowels_and_consonants_empty_string():
    result = find_vowels_and_consonants("")
    assert result == (0, 0)

def test_find_vowels_and_consonants_all_vowels():
    result = find_vowels_and_consonants("aeiou")
    assert result == (5, 0)

def test_find_vowels_and_consonants_mixed_string():
    result = find_vowels_and_consonants("Hello World")
    assert result == (3, 7)

def test_find_vowels_and_consonants_case_insensitive():
    result = find_vowels_and_consonants("PyThOn")
    assert result == (1, 5)
