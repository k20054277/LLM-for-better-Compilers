import requests

# Use the package manager to install the requests library
pip install requests

# Make a request to a URL using the requests library
response = requests.get('https://www.example.com')

# Check if the response was successful
if response.status_code == 200:
    # If the response was successful, print the content of the page
    print(response.content)
else:
    # If the response was not successful, print an error message
    print('Error:', response.status_code)