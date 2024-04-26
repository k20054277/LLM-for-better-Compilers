import asyncio

async def fetch_data(url):
    # Fetch data from a URL using the requests library
    response = await requests.get(url)
    return response.json()

async def main():
    urls = ["https://api.example1.com", "https://api.example2.com"]

    # Use async and slice to fetch data from multiple URLs concurrently
    results = await asyncio.gather(*[fetch_data(url) for url in urls])

    # Print the results
    print(results)

asyncio.run(main())