
# True and venv demonstration

# Import True and venv modules
import true
import venv

# Create a virtual environment
venv.create("my_venv")

# Activate the virtual environment
venv.activate("my_venv")

# Print True and venv version
print(True)
print(venv.__version__)

# Install a package in the virtual environment
pip install pandas

# Import the package from the virtual environment
import pandas

# Print the package version
print(pandas.__version__)

# Deactivate the virtual environment
venv.deactivate()

# Print True and venv version again after deactivation
print(True)
print(venv.__version__)
