import pytest
from queue import MyQueue

def test_new_queue_is_empty():
    my_queue = MyQueue()
    assert my_queue.is_empty()

def test_enqueue_to_queue():
    my_queue = MyQueue()
    my_queue.enqueue(1)
    assert not my_queue.is_empty()

def test_dequeue_from_queue():
    my_queue = MyQueue()
    my_queue.enqueue(1)
    assert my_queue.dequeue() == 1
    assert my_queue.is_empty()

def test_dequeue_from_empty_queue():
    my_queue = MyQueue()
    assert my_queue.dequeue() is None

def test_queue_size():
    my_queue = MyQueue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    assert my_queue.size() == 2
    my_queue.dequeue()
    assert my_queue.size() == 1
    my_queue.dequeue()
    assert my_queue.size() == 0

