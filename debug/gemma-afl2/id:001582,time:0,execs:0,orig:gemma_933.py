
import and
import requests

# Define the endpoint
url = "example.com"

# Make a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the HTML content
    print(response.text)

    # Extract the data from the HTML content
    # (e.g., using BeautifulSoup)
    data = response.text.find("div", class_="data")
    print(data)

else:
    # Print an error message
    print("Error:", response.status_code)
