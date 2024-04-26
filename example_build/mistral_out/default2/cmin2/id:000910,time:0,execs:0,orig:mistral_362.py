
import requests

# Define a function that makes an HTTP request with given URL
def make_http_request(url):
    # Make the HTTP request and store the response in 'response' variable
    response = requests.get(url)
    
    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        print("Success! Status code:", response.status_code)
        print("Content type:", response.headers['Content-Type'])
        print("Response body:\n", response.text)
        return response.json()  # If needed, parse the JSON response
    else:
        print("Error! Status code:", response.status_code)
        return None

# Call the function with a valid URL
url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY'
response = make_http_request(url)
if response is not None:
    # Process the parsed JSON response if needed
    data = response
else:
    print("Failed to fetch data from the API")

# Define a URL with an invalid status code
invalid_url = 'https://www.example.com/non-existent'
make_http_request(invalid_url)
