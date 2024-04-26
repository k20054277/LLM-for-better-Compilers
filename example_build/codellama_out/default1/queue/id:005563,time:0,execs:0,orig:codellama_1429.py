# Create a new virtual environment
$ virtualenv myenv

# Activate the virtual environment
$ source myenv/bin/activate

# Install a package in the virtual environment
(myenv) $ pip install requests

# Import the package in your code
import requests

# Use assert to check that the package is installed correctly
assert requests.get("https://www.example.com").status_code == 200

# Deactivate the virtual environment
(myenv) $ deactivate