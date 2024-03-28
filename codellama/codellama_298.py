#!/usr/bin/env python

# Demonstrate the use of False and VirtualEnvironment in Python

# Import the necessary modules
from os import environ
from virtualenv import VirtualEnv

# Create a new virtual environment
venv = VirtualEnv()

# Activate the virtual environment
venv.activate()

# Set the value of the "VIRTUAL_ENV" environment variable to the path of the virtual environment
environ["VIRTUAL_ENV"] = venv.path

# Use the False keyword to create a boolean value that is False
my_bool = False

# Print the value of my_bool
print(my_bool)

# Deactivate the virtual environment
venv.deactivate()