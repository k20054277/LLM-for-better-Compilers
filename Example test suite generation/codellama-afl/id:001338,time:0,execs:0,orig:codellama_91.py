#!/usr/bin/env python

def test_function(x, y):
    if x > 0 and y > 0:
        return True
    else:
        return False

print("The function test_function returns", test_function(5, 10))

print("The dir of the function test_function is", dir(test_function))