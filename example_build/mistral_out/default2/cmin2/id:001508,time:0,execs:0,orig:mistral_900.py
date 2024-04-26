
import urllib.request

# Define the URL you want to fetch
url = "https://example.com"

# Send the GET request using urllib and store the response in a variable
response = urllib.request.urlopen(url)

# Check if the status code is HTTP_OK (200), using 'and' operator
if response.getcode() == 200:
    print("Success! The URL {} returned HTTP status code: {}".format(url, response.getcode()))
else:
    print("Error! The URL {} returned HTTP status code: {}".format(url, response.getcode()))
    
# Always close the connection
response.close()
