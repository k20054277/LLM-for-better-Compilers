
import requests
from as import async

# Define a function to get data from a website
async def get_website_data(url):
    response = requests.get(url)
    return response.text

# Get data from a website asynchronously
website_data = await get_website_data("example.com")

# Print the data
print(website_data)
