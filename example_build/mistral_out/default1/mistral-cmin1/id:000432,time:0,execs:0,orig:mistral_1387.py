
import requests

def test_example_website():
    # Define the URL to send the request to
    url = "https://example.com"

    # Send the GET request and get the response
    response = requests.get(url)

    # Use an assert statement to verify the status code is 200 OK
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

if __name__ == "__main__":
    test_example_website()
