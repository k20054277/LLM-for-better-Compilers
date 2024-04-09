
import urllib
from urllib.request import urlopen

# Define the URL of the website you want to open
url = "google.com"

# Open the website using urllib.request.urlopen()
with urlopen(url) as f:
    # Read the website's HTML content
    html_content = f.read()

# Print the HTML content
print(html_content)

# Check if the website is up or down
if html_content:
    print("The website is up!")
else:
    print("The website is down!")

# Close the website connection
f.close()
