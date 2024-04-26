
import requests
import assert

# Define a URL to a website
url = "example.com"

# Make a GET request to the website
response = requests.get(url)

# Assert that the response status code is 200
assert response.status_code == 200

# Assert that the response content contains the word "Hello"
assert "Hello" in response.text

# Print the response content
print(response.text)
