#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from formationPython0923.rendu.Matthieu.pytest_src.exemple import add

def test_add():
	assert add(1,3)==4
	assert add(2,3)==1
	assert add(1,-5)==-4

