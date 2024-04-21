
from even_odd_no import filter_even_numbers
from even_odd_no import filter_odd_numbers

#test even no.
def test_filter_even_numbers_empty_list():
    result = filter_even_numbers([])
    assert result == []

def test_filter_even_numbers_no_even_numbers():
    result = filter_even_numbers([1, 3, 5, 7])
    assert result == []

def test_filter_even_numbers_some_even_numbers():
    result = filter_even_numbers([1, 2, 3, 4, 5, 6])
    assert result == [2, 4, 6]

def test_filter_even_numbers_all_even_numbers():
    result = filter_even_numbers([2, 4, 6, 8, 10])
    assert result == [2, 4, 6, 8, 10]

def test_filter_even_numbers_mixed_numbers():
    result = filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert result == [2, 4, 6, 8, 10]




# test_list_odd

def test_filter_odd_numbers_empty_list():
    result = filter_odd_numbers([])
    assert result == []

def test_filter_odd_numbers_no_odd_numbers():
    result = filter_odd_numbers([2, 4, 6, 8])
    assert result == []

def test_filter_odd_numbers_some_odd_numbers():
    result = filter_odd_numbers([1, 2, 3, 4, 5, 6])
    assert result == [1, 3, 5]

def test_filter_odd_numbers_all_odd_numbers():
    result = filter_odd_numbers([1, 3, 5, 7, 9])
    assert result == [1, 3, 5, 7, 9]

def test_filter_odd_numbers_mixed_numbers():
    result = filter_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert result == [1, 3, 5, 7, 9]
