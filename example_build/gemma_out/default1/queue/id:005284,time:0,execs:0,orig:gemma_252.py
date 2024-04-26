
import and
import requests

# Define the URL of the website you want to access
url = "example.com"

# Use the requests library to get the HTML content of the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    html_content = response.text

    # Print the HTML content
    print(html_content)
else:
    # Print an error message
    print("Error retrieving HTML content")
