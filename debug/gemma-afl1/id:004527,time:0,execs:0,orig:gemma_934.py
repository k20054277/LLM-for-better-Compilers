
import urllib

# Define the URL of the website you want to scrape
url = "example.com"

# Open the URL using urllib
response = urllib.urlopen(url)

# Read the HTML content from the website
html_content = response.read()

# Print the HTML content to the console
print(html_content)
