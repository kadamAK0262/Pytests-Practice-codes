import pytest
from count_vowels_consonants import find_vowels_consonants

# Test case for an empty string
def test_find_vowels_consonants_empty_string():
    input_string = ""
    assert find_vowels_consonants(input_string) == (0, 0)

# Test case for a string with only vowels
def test_find_vowels_consonants_only_vowels():
    input_string = "aeiou"
    assert find_vowels_consonants(input_string) == (5, 0)

# Test case for a string with only consonants
def test_find_vowels_consonants_only_consonants():
    input_string = "bcdfg"
    assert find_vowels_consonants(input_string) == (0, 5)

# Test case for a string with both vowels and consonants
def test_find_vowels_consonants_both_vowels_and_consonants():
    input_string = "hello world"
    assert find_vowels_consonants(input_string) == (3, 7)

# Test case for a string with uppercase and lowercase letters
def test_find_vowels_consonants_uppercase_and_lowercase():
    input_string = "Hello World"
    assert find_vowels_consonants(input_string) == (3, 7)
