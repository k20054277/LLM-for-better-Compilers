import requests

url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    print("The server is alive!")
else:
    print("The server is not responding.")