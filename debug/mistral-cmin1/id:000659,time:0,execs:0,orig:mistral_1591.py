
import asyncio
import aiohttp

# List of URLs to fetch data from
urls = ["https://example.com", "https://another-example.com", "https://yet-another-example.com"]

async def fetch(session, url):
    """Asynchronous function to fetch data from a given URL."""
    async with session.get(url) as response:
        return await response.text()

async def main():
    """Main function to orchestrate the fetching of data from multiple URLs."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

        print("Responses:")
        for i, response in enumerate(responses):
            print(f"URL {i + 1}: {response}")

if __name__ == "__main__":
    asyncio.run(main())
