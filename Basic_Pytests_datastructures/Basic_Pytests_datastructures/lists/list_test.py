import pytest
from list import MyList

def test_list_append():
    my_list = MyList()
    my_list.append(1)
    my_list.append(2)
    assert my_list.items == [1, 2]

def test_list_index():
    my_list = MyList()
    my_list.append(1)
    my_list.append(2)
    assert my_list.index(2) == 1

def test_list_remove():
    my_list = MyList()
    my_list.append(1)
    my_list.append(2)
    my_list.remove(2)
    assert my_list.items == [1]

# def test_list_pop():
#     my_list = MyList()
#     my_list.append(1)
#     my_list.append(2)
#     assert my_list.pop() == 2
#     assert my_list.items == [1]
def test_list_pop():
    my_list = MyList()
    my_list.append(1)
    my_list.append(2)
    assert my_list.pop() == 2
    assert my_list.items == [1]

def test_list_pop_from_empty():
    my_list = MyList()
    with pytest.raises(IndexError, match="pop from empty list"):
        my_list.pop()



def test_list_count():
    my_list = MyList()
    my_list.extend([1, 2, 1, 3, 1])
    assert my_list.count(1) == 3

def test_list_clear():
    my_list = MyList()
    my_list.extend([1, 2, 3])
    my_list.clear()
    assert my_list.items == []

def test_list_reverse():
    my_list = MyList()
    my_list.extend([1, 2, 3])
    my_list.reverse()
    assert my_list.items == [3, 2, 1]

def test_list_extend():
    my_list = MyList()
    my_list.extend([1, 2])
    my_list.extend([3, 4])
    assert my_list.items == [1, 2, 3, 4]
