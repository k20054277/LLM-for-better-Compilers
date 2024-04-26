# This code snippet creates a virtual environment using the venv module in Python
import venv

# Create a new virtual environment
venv.create('myenv')

# Activate the virtual environment
venv.activate('myenv')

# Install packages in the virtual environment
pip install requests

# Deactivate the virtual environment
venv.deactivate()