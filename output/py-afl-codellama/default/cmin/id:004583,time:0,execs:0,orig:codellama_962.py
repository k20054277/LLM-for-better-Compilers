import requests

# Make a request to a website and check if it was successful
response = requests.get("https://www.example.com")
if response.status_code == 200 and "success" in response.text:
    print("The website is up and running!")
else:
    print("The website is not working properly.")