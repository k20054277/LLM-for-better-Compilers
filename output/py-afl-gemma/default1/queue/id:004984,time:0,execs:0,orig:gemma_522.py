
# Import libraries
import virtualenv
from virtualenv import ensure_pip

# Create a virtual environment
virtualenv.create('my_venv')

# Activate the virtual environment
ensure_pip('my_venv')

# Install packages in the virtual environment
virtualenv.pip('requests')

# Use packages from the virtual environment
import requests

# Make a GET request
response = requests.get('google.com')

# Print the response
print(response.text)

# Deactivate the virtual environment
virtualenv.deactivate()

# Print a message after deactivating the virtual environment
print('Virtual environment deactivated')
