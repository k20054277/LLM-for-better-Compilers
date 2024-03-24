import requests

# Make a GET request to a URL and print the response
response = requests.get('https://www.example.com')
print(response.text)

# Check if the status code is 200 (OK)
if response.status_code == 200:
    # Print the response text
    print(response.text)
else:
    # Print an error message
    print("Error: " + str(response.status_code))