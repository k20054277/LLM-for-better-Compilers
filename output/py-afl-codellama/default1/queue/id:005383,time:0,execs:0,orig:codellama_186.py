#!/usr/bin/env python

def my_function(x):
    if x > 0:
        return True
    else:
        raise ValueError("x must be positive")

try:
    result = my_function(-1)
except ValueError as e:
    print("Caught an exception:", e)
else:
    print("No exceptions caught, result is", result)