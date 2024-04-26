
import urllib

# Open a URL using urllib
url = "example.com"
response = urllib.urlopen(url)

# Read the HTML content
html_content = response.read()

# Print the HTML content
print(html_content)

# Close the URL connection
response.close()
