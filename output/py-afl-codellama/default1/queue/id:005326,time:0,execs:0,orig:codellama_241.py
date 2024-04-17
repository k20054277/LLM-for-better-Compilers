import requests

# Make a GET request to a URL
response = requests.get("https://example.com")

# Check if the response was successful (i.e., status code 200)
if response.status_code == 200:
    print("Request successful!")
else:
    print("Request failed with status code", response.status_code)

# Use False to check if a variable is False
x = False
if x:
    print("x is True")
else:
    print("x is False")