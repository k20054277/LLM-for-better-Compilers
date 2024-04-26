
# Import the necessary libraries
from bs4 import BeautifulSoup
import requests

# Make a request to the website
url = "https://example.com"
r = requests.get(url)

# Check if the request was successful (status code 200)
if r.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Use BeautifulSoup to find elements on the page
    title = soup.title
    print("Page title:", title)
    
    # Perform other actions based on your needs (e.g., extract data from specific HTML tags)
else:
    print(f"Request failed with status code {r.status_code}")
