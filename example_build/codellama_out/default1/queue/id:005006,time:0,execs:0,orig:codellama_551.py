# Import the necessary modules
import os
import sys
from virtualenv import VirtualEnv

# Create a new virtual environment
venv = VirtualEnv(os.path.join(os.getcwd(), 'my_venv'))

# Activate the virtual environment
venv.activate()

# Install the necessary packages
venv.install('numpy')
venv.install('scipy')

# Use None in a Python program
print("None is", None)