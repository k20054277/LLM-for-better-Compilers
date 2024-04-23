#!/usr/bin/python3

# Create a new virtual environment named "myenv"
python -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install a package that uses False
pip install package-with-false

# Use the package in your code
from package_with_false import use_false

# Test the package with the `False` value
result = use_false(False)
print(result)

# Deactivate the virtual environment
deactivate myenv