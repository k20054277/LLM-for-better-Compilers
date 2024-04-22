#!/usr/bin/env python

def my_function(x):
    if x > 0 and x < 10:
        print("The value of x is between 0 and 10.")
    elif x == 10:
        print("The value of x is equal to 10.")
    else:
        print("The value of x is not between 0 and 10.")

# Test the function with different values for x
my_function(5)   # Output: The value of x is between 0 and 10.
my_function(15)  # Output: The value of x is not between 0 and 10.
my_function(10)  # Output: The value of x is equal to 10.