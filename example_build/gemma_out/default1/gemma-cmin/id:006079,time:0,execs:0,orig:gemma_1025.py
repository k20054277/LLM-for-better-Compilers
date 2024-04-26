
import os
import sys

# Define a function to demonstrate the use of and and process
def my_function(a, b):
    # Use and operator to check if a and b are both true
    if a and b:
        print("a and b are both true")

    # Use process module to execute a command
    os.system("ls -l")

# Call the function with two true values
my_function(True, True)

# Call the function with one true and one false value
my_function(True, False)

# Call the function with two false values
my_function(False, False)
