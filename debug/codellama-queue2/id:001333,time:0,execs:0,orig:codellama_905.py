import requests

# Set the URL for the API call
url = "https://api.example.com/data"

# Make the GET request
response = requests.get(url)

# Check if the response was successful (status code 200)
if response.status_code == 200:
    # Print the response data
    print(response.json())
else:
    # Print an error message if the response was not successful
    print("An error occurred when making the GET request")