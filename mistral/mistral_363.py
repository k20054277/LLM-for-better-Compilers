
import urllib.request

# Function that sends a GET request to the given URL and handles None response
def send_request(url):
    try:
        response = urllib.request.urlopen(url)
        if response:
            data = response.read().decode('utf-8')
            return data
        else:
            print("Server returned an empty response")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# URL of the imaginary API
url = "http://example.com/api"

# Call the send_request function and handle the None response if needed
response = send_request(url)

if response is not None:
    # Process the data returned by the API
    print("Data received from API:")
    print(response)
else:
    print("No data received from API")
