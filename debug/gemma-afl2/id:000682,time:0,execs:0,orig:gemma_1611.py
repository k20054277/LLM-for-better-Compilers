
import asyncio

async def fetch_data(url):
    # Simulate fetching data asynchronously
    await asyncio.sleep(0.5)
    return url + " data"

async def main():
    # Create a list of URLs
    urls = ["url1", "url2", "url3"]

    # Use filter and async to fetch data and filter out errors
    results = await asyncio.gather(
        filter(fetch_data, urls)
    )

    # Print the results
    print(results)

asyncio.run(main())
