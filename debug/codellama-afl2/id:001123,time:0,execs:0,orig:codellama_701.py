# This program demonstrates the use of "True" and "logging" in Python

import logging

# Set up logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Define a function that returns True
def my_function():
    return True

# Log the output of the function
logging.info("The value of my_function() is: %s", my_function())