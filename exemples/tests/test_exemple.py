#! /usr/bin/env python3

from src.exemple import add, multiply

import pytest

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0), (-1, -1, -2)])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    
    
def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(0, 0) == 0
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1