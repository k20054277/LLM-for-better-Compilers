
import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "example.com"

# Get the HTML content of the website
response = requests.get(url)

# Parse the HTML content into a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Find all the elements you want to scrape
elements = soup.find_all("div", class_="article-content")

# Iterate over the elements and print their text content
for element in elements:
    print(element.text)

# Print the number of elements found
print(len(elements))
