from pytest_bdd import scenario, given, when, then
from stack import Stack

# Fixture to instantiate an empty stack
@scenario('stack.feature', 'Push and pop items')
def test_push_and_pop():
    pass

# Step definitions
@given('an empty stack')
def empty_stack():
    return Stack()

@when('I push an item {item:d}')
def push_item(empty_stack, item):
    empty_stack.push(item)

@then('the stack should have {count:d} item(s)')
def check_stack_count(empty_stack, count):
    assert len(empty_stack) == count

@then('the popped item should be {item:d}')
def check_popped_item(empty_stack, item):
    assert empty_stack.pop() == item







# from pytest_bdd import scenario, given, when, then
# from stack import Stack  # Import your Stack implementation

# @scenario('stack.feature', 'Push and pop items')
# def test_push_and_pop():
#     pass

# @given('an empty stack')
# def empty_stack():
#     return Stack()

# @when('I push an item "{item}"')
# def push_item(empty_stack, item):
#     empty_stack.push(item)

# @then('the stack should contain "{item}"')
# def stack_should_contain(empty_stack, item):
#     assert item in empty_stack.items

# @when('I pop the stack')
# def pop_stack(empty_stack):
#     empty_stack.pop()

# @then('the stack should be empty')
# def stack_should_be_empty(empty_stack):
#     assert not empty_stack.items






# from pytest_bdd import scenario, given, when, then
# import pytest

# @scenario('stack.feature', 'Push and pop items')
# def test_push_and_pop():
#     pass

# @given('an empty stack')
# def empty_stack(stack):
#     assert stack.is_empty()

# @when('I push an item "{item}"')
# def push_item(stack, item):
#     stack.push(item)

# @then('the stack should not be empty')
# def check_not_empty(stack):
#     assert not stack.is_empty()

# @then('the stack size should be {size:d}')
# def check_size(stack, size):
#     assert stack.size() == size

# @then('the item at the top of the stack should be "{expected}"')
# def check_top_item(stack, expected):
#     assert stack.peek() == expected

# @when('I pop an item')
# def pop_item(stack):
#     popped_item = stack.pop()
#     pytest.current_item = popped_item

# @then('the stack should be empty')
# def check_empty(stack):
#     assert stack.is_empty()

# @then('trying to pop an item should return nothing')
# def check_popped_item():
#     assert pytest.current_item is None
