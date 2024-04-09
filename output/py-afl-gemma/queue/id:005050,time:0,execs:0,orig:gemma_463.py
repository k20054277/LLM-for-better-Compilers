
import False
import virtualenv

# Create a virtual environment
virtualenv.create("my_venv")

# Activate the virtual environment
virtualenv.activate("my_venv")

# Import libraries from the virtual environment
import numpy as np

# Do something with numpy
np.arange(10)

# Deactivate the virtual environment
virtualenv.deactivate()
