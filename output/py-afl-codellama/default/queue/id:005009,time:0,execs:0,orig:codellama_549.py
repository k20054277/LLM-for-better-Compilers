import pip

print(None)  # Output: None

# Install requests module using pip
pip.main(['install', 'requests'])

# Import requests module
from requests import get

# Use get method to make a GET request to the specified URL
response = get('https://www.example.com')

# Print the status code of the response
print(response.status_code)