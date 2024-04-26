
import requests

# Example URL to check
url = "https://www.example.com"

# Using if statement with 'and' operator
if requests.get(url).status_code == 200 and "200 OK" in requests.get(url).reason:
    print(f"The website '{url}' is accessible and returns status code: 200")
else:
    print(f"Error accessing the website '{url}'. Check status code: {requests.get(url).status_code}")

# Using one-liner with 'and' operator
if (requests.get(url).status_code == 200) and ("200 OK" in requests.get(url).reason):
    print(f"The website '{url}' is accessible and returns status code: 200")
else:
    print(f"Error accessing the website '{url}'. Check status code: {requests.get(url).status_code}")
