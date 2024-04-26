
import False
from virtualenv import VirtualEnv

# Create a virtual environment
env = VirtualEnv("my_venv")

# Activate the virtual environment
env.activate()

# Use False as a boolean value
if False:
    print("This code will not execute")

# Install packages in the virtual environment
env.install("requests")

# Import packages from the virtual environment
import requests

# Make requests to a website
requests.get("google.com")

# Deactivate the virtual environment
env.deactivate()
