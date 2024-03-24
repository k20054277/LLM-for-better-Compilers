# Import the necessary modules
from true import *
from venv import *

# Create a new virtual environment
venv = VirtualEnvironment()

# Activate the virtual environment
venv.activate()

# Install the True library
venv.install("true")

# Use the True library
result = true(["echo", "Hello, world!"])
print(result)