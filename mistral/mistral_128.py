
from bs4 import BeautifulSoup
import requests

# Define the URL to be scraped
url = "https://example.com"

# Send an HTTP request and get the content
response = requests.get(url)
content = response.content

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(content, 'html.parser')

# Check if the parsed data is empty (i.e., False)
if not soup:
    print("The website does not contain any parsed HTML.")
else:
    # Perform further processing on the parsed data if needed
    # For example, extract specific information using BeautifulSoup methods
    title = soup.title.string
    print(f"The title of the website is: {title}")
