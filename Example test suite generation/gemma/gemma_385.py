
import urllib

# Define a False boolean value
is_true = False

# Use False to control the flow of the program
if is_true:
    print("This code will not execute")

# Use False to prevent the urllib.urlopen function from opening the URL
url = "example.com"
urllib.urlopen(url, None, timeout=1)
