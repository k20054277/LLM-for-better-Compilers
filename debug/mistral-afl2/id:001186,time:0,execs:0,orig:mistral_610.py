
import requests

# Define the URL to be accessed
url = "https://www.google.com"

# Send an HTTP request using GET method and store the response in a variable
response = requests.get(url)

# Check if the request was successful (status code is 200)
if response.status_code == 200:
    print("Website is accessible")
else:
    print(f"Website {url} is not accessible, status code: {response.status_code}")

# Use True to check if a condition is met (in this case, the website is accessible)
if True:
    print("This condition is always true and will be executed")
