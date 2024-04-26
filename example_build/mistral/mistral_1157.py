
from bs4 import BeautifulSoup, Tag
import requests

# Send a GET request to the URL and get the content
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
page_content = requests.get(url).content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, "html.parser")

# Select the first h2 tag with the class 'mw-headline' and assign it an alias
heading = soup.find('h2', class_='mw-headline') as python_heading
print(f"Python programming language: {python_heading.text}")

# Select all li tags with the class 'reflist' and assign them a list alias
reference_lists = soup.find_all('li', class_='reflist') as reference_lists

for ref_list in reference_lists:
    print("References for this section:")
    links = ref_list.find_all('a')
    for link in links:
        print(link['href'])
