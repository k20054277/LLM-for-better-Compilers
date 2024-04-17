import requests
from bs4 import BeautifulSoup

# Make a request to the website and get the HTML response
url = "https://www.example.com"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the specific element you want to extract data from
element = soup.find("div", {"id": "some_id"})

# Use the "as" keyword to convert the element into a different type
text = element.text.strip()
print(text)