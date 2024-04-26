
# Import necessary libraries
import os
import pip

# Create a virtual environment
venv = virtualenv.create('my_venv')

# Activate the virtual environment
venv.activate()

# Install dependencies from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

for req in requirements:
    pip.install(req)

# Use the libraries from the virtual environment
print('Using libraries from the virtual environment:')
print(os.listdir('my_venv/lib/python3.6/site-packages'))

# Deactivate the virtual environment
venv.deactivate()
