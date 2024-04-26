
import asyncio
import aiohttp

# Define a function to fetch data from a URL asynchronously
async def fetch(url):
    print(f"Fetching data from {url}")
    async with aiohttp.Client() as client:
        async with client.get(url) as response:
            data = await response.text()
            return data

# Define two URLs to fetch data from
urls = [
    "https://www.example1.com",
    "https://www.example2.com"
]

# Create a list of tasks to fetch data asynchronously
tasks = [asyncio.create_task(fetch(url)) for url in urls]

# Use asyncio's gather function to wait for all tasks to complete and collect their results
results = await asyncio.gather(*tasks)

# Print fetched data
for i, result in enumerate(results):
    print(f"\nData from URL {i+1}:")
    print(result)
