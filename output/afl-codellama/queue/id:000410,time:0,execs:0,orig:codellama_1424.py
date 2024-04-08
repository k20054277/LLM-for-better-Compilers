# Create a new virtual environment for this project
python -m venv my_project

# Activate the virtual environment
source my_project/bin/activate

# Install the necessary packages
pip install requests

# Import the requests library
import requests

# Use assert to check that the response status code is 200
response = requests.get("https://www.example.com")
assert response.status_code ==