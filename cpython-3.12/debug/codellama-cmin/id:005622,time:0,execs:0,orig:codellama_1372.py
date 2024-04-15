import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Use assert to check if the response was successful
assert response.ok

# Extract the title of the website using BeautifulSoup
title = soup.find("title").text
print(title)