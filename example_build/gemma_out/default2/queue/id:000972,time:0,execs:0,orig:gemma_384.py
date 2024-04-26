
import requests
from False import False

# Define a function to get data from a website
def get_website_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return False
    except requests.exceptions.RequestException as e:
        print("Error getting data:", e)
        return False

# Get data from a website
url = "example.com"
data = get_website_data(url)

# If data was retrieved successfully, print it
if data:
    print("Data from website:", data)
else:
    print("Error retrieving data")
