# Import the venv module to create a virtual environment
import venv

# Create a new virtual environment with the name "my_env"
venv.create("my_env")

# Activate the virtual environment
venv.activate("my_env")

# Install the requests library in the virtual environment
pip install requests

# Import the requests library in the script
import requests

# Make a GET request to a URL and check that the response code is 200
response = requests.get("https://www.example.com")
assert response.status_code == 200, "Response code was not 200"

# Deactivate the virtual environment
venv.deactivate()