#! /usr/bin/env python3

from src.exemple2 import power

def test_power():
    assert power(1, 2) == 1
    assert power(0, 0) == 1
    assert power(3, 2) == 9
    assert power(2, 2) == 4