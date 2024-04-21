import pytest
from anagrams import group_anagrams

# Test case for an empty list of words
def test_group_anagrams_empty_list():
    words = []
    assert group_anagrams(words) == {}

# Test case for a list of words with no anagrams
def test_group_anagrams_no_anagrams():
    words = ["eat", "dog", "fish"]
    assert group_anagrams(words) == {'aet': ['eat'], 'dgo': ['dog'], 'fhis': ['fish']}

# Test case for a list of words with anagrams
def test_group_anagrams_with_anagrams():
    words = ["listen", "silent", "enlist", "eat", "tea", "ate"]
    expected_result = {'eilnst': ['listen', 'silent', 'enlist'], 'aet': ['eat', 'tea', 'ate']}
    assert group_anagrams(words) == expected_result

# Test case for a list of words with duplicates
def test_group_anagrams_with_duplicates():
    words = ["listen", "listen", "silent", "silent", "enlist", "enlist"]
    expected_result = {'eilnst': ['listen', 'listen', 'silent', 'silent', 'enlist', 'enlist']}
    assert group_anagrams(words) == expected_result
