#!/usr/bin/env python

# This program checks if a user input is a valid integer

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print("Enter an integer: ")

# Get the user's input
user_input = input()

# Check if the input is a valid integer
if is_integer(user_input):
    print("The input is a valid integer.")
else:
    print("The input is not a valid integer.")