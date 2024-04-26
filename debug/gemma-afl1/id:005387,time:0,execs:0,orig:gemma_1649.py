
import asyncio
import sorted

async def fetch_data(url):
    # Simulate fetching data asynchronously
    await asyncio.sleep(0.5)
    return url, random.randint(1, 10)

async def main():
    # Create a list of URLs
    urls = ["url1", "url2", "url3", "url4"]

    # Fetch data asynchronously and sort by second value
    results = await sorted(fetch_data(url) for url in urls)

    # Print the results
    for url, data in results:
        print(f"URL: {url}, Data: {data}")

asyncio.run(main())
