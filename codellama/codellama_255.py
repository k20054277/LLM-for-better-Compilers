#!/usr/bin/env python

def my_function(x):
    if x > 0:
        return True
    else:
        return False

def test_my_function():
    assert my_function(1) == True
    assert my_function(-1) == False