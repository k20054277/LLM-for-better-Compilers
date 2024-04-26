
import asyncio
import aiohttp

# Define a coroutine to fetch a single website URL
async def fetch_website(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status in (200, 301):
                return url

# Define a list of URLs to fetch
urls = [
    "https://example.com",
    "https://google.com",
    "https://microsoft.com"
]

# Define a coroutine that fetches all the URLs and sorts the results
async def main():
    tasks = [fetch_website(url) for url in urls]
    websites = await asyncio.gather(*tasks)
    sorted_websites = sorted(websites)

    print("Fetched and sorted websites:")
    for website in sorted_websites:
        print(website)

# Run the main coroutine
asyncio.run(main())
