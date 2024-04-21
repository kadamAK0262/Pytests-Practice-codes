from pytest_bdd import given, when, then
from arrays import MyArray

@given("a new array")
def new_array():
    return MyArray()

@when("I append {item} to the array")
def append_item_to_array(new_array, item):
    new_array.append(int(item))

@when("I remove {item} from the array")
def remove_item_from_array(new_array, item):
    new_array.remove(int(item))

@when("I get item at index {index}")
def get_item_at_index(new_array, index):
    index = int(index)
    new_array.result = new_array.get_item_at_index(index)

@then("the array should be empty")
def array_should_be_empty(new_array):
    assert new_array.is_empty()

@then("the array should not be empty")
def array_should_not_be_empty(new_array):
    assert not new_array.is_empty()

@then("it should be {expected}")
def it_should_be(new_array, expected):
    assert new_array.result == int(expected)

@then("the size of the array should be {size}")
def size_of_array_should_be(new_array, size):
    assert new_array.size() == int(size)
