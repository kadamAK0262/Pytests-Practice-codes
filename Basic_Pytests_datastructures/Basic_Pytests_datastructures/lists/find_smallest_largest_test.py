from find_smallest_largest import find_smallest_largest

def test_find_smallest_largest():
    my_list = [5, 2, 8, 1, 9, 3]
    smallest, largest = find_smallest_largest(my_list)
    assert smallest == 1
    assert largest == 9

    # Test with an empty list
    my_empty_list = []
    smallest, largest = find_smallest_largest(my_empty_list)
    assert smallest is None
    assert largest is None

    # Test with a list containing only one element
    my_single_element_list = [10]
    smallest, largest = find_smallest_largest(my_single_element_list)
    assert smallest == 10
    assert largest == 10

    # Test with a list containing negative numbers
    my_negative_list = [-5, -2, -8, -1, -9, -3]
    smallest, largest = find_smallest_largest(my_negative_list)
    assert smallest == -9
    assert largest == -1