# Create a new virtual environment
python -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install packages into the virtual environment
pip install requests

# Use the installed package in your code
import requests
response = requests.get('https://www.example.com')
print(response.text)

# Deactivate the virtual environment
deactivate