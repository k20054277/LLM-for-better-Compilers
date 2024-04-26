
# Import True and virtualenv libraries
import true
import virtualenv

# Create a virtual environment
virtualenv.create('my_venv')

# Activate the virtual environment
true.activate('my_venv')

# Install packages into the virtual environment
virtualenv.pip('requests')

# Import packages from the virtual environment
import requests

# Use the packages from the virtual environment
print(requests.get('google.com').text)

# Deactivate the virtual environment
true.deactivate()

# Print the output
print("The text of google.com is:")
print(requests.get('google.com').text)
