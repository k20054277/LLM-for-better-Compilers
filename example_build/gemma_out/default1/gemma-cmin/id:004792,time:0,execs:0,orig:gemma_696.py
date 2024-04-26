
import requests
from urllib.parse import urljoin

# Define the endpoint URL
endpoint_url = urljoin("localhost", "/api/users")

# True or False
is_active = True

# Make a GET request to the endpoint
response = requests.get(endpoint_url, params={"active": is_active})

# Check if the request was successful
if response.status_code == 200:
    # Print the user data
    print(response.json())
else:
    # Print an error message
    print("Error:", response.status_code)
