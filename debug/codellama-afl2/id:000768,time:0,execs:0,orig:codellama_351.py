# Create a new file named "test.py"
$ touch test.py

# Open the file in your favorite text editor
$ nano test.py

# Add the following code to the file
print("Hello, world!")

# Save and close the file

# Use the package manager pip to install the requests library
$ pip install requests

# Import the requests library in your Python script
from requests import get

# Make an HTTP GET request to a website
response = get("https://www.example.com")

# Print the response status code and content
print(f"Status code: {response.status_code}")
print(f"Content: {response.content}")