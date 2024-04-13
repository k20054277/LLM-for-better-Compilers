import urllib.request

# Open the URL using urllib.request.urlopen() method
with urllib.request.urlopen("https://www.example.com") as response:
    # Read the contents of the URL
    data = response.read()

    # Print the contents of the URL
    print(data)