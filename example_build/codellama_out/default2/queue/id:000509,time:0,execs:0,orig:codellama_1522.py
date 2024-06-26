import asyncio
from concurrent.futures import ThreadPoolExecutor

async def fetch_url(url):
    # Make a request to the URL and return the response
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()

# Set up an executor to run the fetch_url function in parallel
executor = ThreadPoolExecutor(max_workers=5)

# Create a list of URLs to fetch
urls = ['http://example.com', 'https://www.python.org', 'https://www.google.com']

# Use the executor to run the fetch_url function in parallel
futures = [executor.submit(fetch_url, url) for url in urls]

# Wait for all of the futures to complete
results = await asyncio.gather(*futures)

# Print the results
for result in results:
    print(result)