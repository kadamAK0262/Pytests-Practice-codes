import pytest
from stack import Stack  # Replace 'your_module' with the actual module where the Stack class is defined

@pytest.fixture
def empty_stack():
    return Stack()

@pytest.fixture
def filled_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack

def test_new_stack_is_empty(empty_stack):
    assert empty_stack.is_empty()
    assert empty_stack.size() == 0

def test_push_to_stack(empty_stack):
    empty_stack.push(42)
    assert not empty_stack.is_empty()
    assert empty_stack.size() == 1
    assert empty_stack.peek() == 42

def test_pop_from_stack(filled_stack):
    item = filled_stack.pop()
    assert item == 3
    assert filled_stack.size() == 2

def test_peek_at_stack(filled_stack):
    top_item = filled_stack.peek()
    assert top_item == 3
    assert filled_stack.size() == 3

# def test_pop_from_empty_stack(empty_stack):
#     with pytest.raises(IndexError, match="pop from empty list"):
#         empty_stack.pop()
    
def test_pop_from_empty_stack(empty_stack):
    popped_item = empty_stack.pop()
    assert popped_item is None  # or assert popped_item == some_default_value


def test_peek_at_empty_stack(empty_stack):
    assert empty_stack.peek() is None
    assert empty_stack.size() == 0
