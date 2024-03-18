#!/usr/bin/env python

def my_function():
    return False

try:
    if my_function():
        print("This should not be printed")
except Exception as e:
    print(e)