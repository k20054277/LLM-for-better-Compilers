# Import the necessary modules
import sys
from venv import create_virtualenv, run_program

# Create a new virtual environment
venv = create_virtualenv('myenv')

# Install a package in the virtual environment
venv.install('requests')

# Run a program within the virtual environment
run_program(venv, 'python', '-c', 'import requests; print(requests.__version__)')