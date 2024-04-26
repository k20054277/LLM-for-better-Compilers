
import urllib

# Define the URL of the website you want to scrape
url = "example.com"

# Use the urllib library to open the website
response = urllib.urlopen(url)

# Read the website's HTML content
html_content = response.read()

# Close the website connection
response.close()

# Print the HTML content
print(html_content)
