
import requests
from bs4 import BeautifulSoup

# Fetch URL content using requests
url = "https://www.example.com"
response = requests.get(url)

# Check if status_code indicates successful response
if response.status_code != 200:
    print("Error in fetching URL content")
else:
    # Use BeautifulSoup to parse HTML content from the fetched data
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get specific HTML elements using their tags and use as for variable assignments
    title_tag = soup.title
    print("Page Title:")
    print(title_tag.string)

    links = soup.find_all('a')
    print("\nList of all the hyperlinks present in the webpage:")
    for link in links:
        link_url = link.get('href')
        print(link_url)
