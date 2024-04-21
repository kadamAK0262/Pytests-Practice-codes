import pytest
from arrays import MyArray

def test_new_array_is_empty():
    my_array = MyArray()
    assert my_array.is_empty()

def test_append_to_array():
    my_array = MyArray()
    my_array.append(1)
    assert not my_array.is_empty()

def test_remove_from_array():
    my_array = MyArray()
    my_array.append(1)
    my_array.remove(1)
    assert my_array.is_empty()

def test_get_item_at_index():
    my_array = MyArray()
    my_array.append(1)
    my_array.append(2)
    assert my_array.get_item_at_index(0) == 1
    assert my_array.get_item_at_index(1) == 2

def test_get_item_at_invalid_index():
    my_array = MyArray()
    assert my_array.get_item_at_index(0) is None

def test_array_size():
    my_array = MyArray()
    my_array.append(1)
    my_array.append(2)
    assert my_array.size() == 2
    my_array.remove(1)
    assert my_array.size() == 1
    my_array.remove(2)
    assert my_array.size() == 0


