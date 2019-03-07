from stack import Stack
import pytest


def test_push():
    s = Stack(4)
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.stack == [1, 2, 3]


def test_pop():
    s = Stack(4)
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.stack == [1, 2]

def test_full():
    s = Stack(4)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    assert s.stack == [2, 3, 4, 5]

def test_empty():
    s = Stack(4)
    s.push(1)
    s.pop()
    with pytest.raises(IndexError) as e:
        popped = s.pop()
