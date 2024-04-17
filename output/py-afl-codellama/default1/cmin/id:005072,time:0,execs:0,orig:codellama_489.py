import requests

# Make an HTTP GET request to a URL and print the response
response = requests.get('https://api.example.com')
print(response.text)

# Use the None type to represent absence of value
x = None
if x is not None:
    print("Value of x is:", x)
else:
    print("x is None")