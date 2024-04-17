import urllib.request

# send a request to the website and get the response
url = "https://www.example.com"
response = urllib.request.urlopen(url)

# check if the status code of the response is 200 (OK)
if response.getcode() == 200:
    print("The website is up and running!")
else:
    print("The website is down or the URL is incorrect.")