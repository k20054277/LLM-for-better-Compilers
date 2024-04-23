import requests
from bs4 import BeautifulSoup

# Send a request to the website
url = "https://www.example.com"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Print the href attribute of each link
for link in links:
    print(link.get('href'))