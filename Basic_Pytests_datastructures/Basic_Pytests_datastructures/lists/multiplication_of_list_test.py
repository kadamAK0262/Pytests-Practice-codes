from multiplication_of_list import multiply_elements

def test_multiply_elements():
    my_list = [1, 2, 3, 4, 5]
    assert multiply_elements(my_list) == 120

    # Test with an empty list
    assert multiply_elements([]) == 1

    # Test with a list containing only one element
    assert multiply_elements([10]) == 10

    # Test with a list containing negative numbers
    assert multiply_elements([-1, -2, -3, -4, -5]) == -120

    # Test with a list containing floats
    assert multiply_elements([1.5, 2.5, 3.5]) == 13.125

    # Test with a list containing zero
    assert multiply_elements([0, 1, 2, 3]) == 0
