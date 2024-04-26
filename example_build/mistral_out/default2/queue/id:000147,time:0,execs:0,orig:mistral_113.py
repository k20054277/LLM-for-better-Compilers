
import requests

# Set the URL to send a request to (this URL does not exist)
url = "http://nonexistent.url/doesnotexist"

# Send the GET request and assign the response to a variable
response = requests.get(url)

# Check if the status code of the response is 200 OK (which would mean the URL exists and the request was successful)
if response.status_code == 200:
    print("The URL exists and we received a successful response")
else:
    print(f"The URL {url} does not exist or the request failed with status code {response.status_code}")

# The following line will always be executed, regardless of the result of the previous if statement
print("Program completed")

# Since we know the URL does not exist, we expect a False response from the if statement
# This is just to demonstrate that False can be used in Python like any other boolean value
if response.status_code != 200:
    print("The condition is False")
