# test_set_
from set_dictionary_code import get_unique_elements, set_intersection, set_union
from set_dictionary_code import merge_dicts, get_dict_keys

def test_get_unique_elements_empty_set():
    result = get_unique_elements(set())
    assert result == set()

def test_get_unique_elements_non_empty_set():
    result = get_unique_elements({1, 2, 2, 3, 4, 4, 5})
    assert result == {1, 2, 3, 4, 5}

def test_set_intersection():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    result = set_intersection(set1, set2)
    assert result == {4, 5}

def test_set_union():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    result = set_union(set1, set2)
    assert result == {1, 2, 3, 4, 5, 6, 7, 8}


# test_dictionary

def test_merge_dicts():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    result = merge_dicts(dict1, dict2)
    assert result == {'a': 1, 'b': 3, 'c': 4}

def test_get_dict_keys_empty_dict():
    result = get_dict_keys({})
    assert result == []

def test_get_dict_keys_non_empty_dict():
    result = get_dict_keys({'a': 1, 'b': 2, 'c': 3})
    assert result == ['a', 'b', 'c']
