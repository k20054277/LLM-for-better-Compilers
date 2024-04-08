
import BeautifulSoup
import requests

# Define the URL of the website
url = "example.com"

# Make a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.text, "html.parser")

# Find all the articles on the website
articles = soup.find_all("article")

# Print the title of each article
for article in articles:
    print(article.find("h2").text)

# Print the content of each article
for article in articles:
    print(article.find("p").text)

# Print the URL of each article
for article in articles:
    print(article.find("a")["href"])
