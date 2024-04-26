
import requests
import json

def test_api():
    """Tests the API endpoint."""

    # Make a request to the API endpoint
    response = requests.get("https://api.example.com/data")

    assert response.status_code == 200, "API returned an error status code"

    # Verify the response data is as expected
    data = json.loads(response.text)
    assert len(data) > 0, "Received empty data from API"

if __name__ == "__main__":
    test_api()
