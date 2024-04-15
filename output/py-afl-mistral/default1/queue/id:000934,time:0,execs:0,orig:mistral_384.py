
import asyncio
import aiohttp

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            if response.status in (200, 301, 302):
                return await response.text()
            else:
                print(f"Error {response.status}: URL {url} not found or returned an error")
                return None
    except Exception as e:
        print(f"An error occurred while fetching from {url}: {str(e)}")
        return None

async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            "http://google.com",
            "http://example.com/nonexistent_page",
            "https://www.python.org",
            "http://invalid_url"
        ]
        tasks = []
        for url in urls:
            tasks.append(asyncio.create_task(fetch(session, url)))
        
        results = await asyncio.gather(*tasks)

        print("\nResults:")
        for i, result in enumerate(results):
            if result is not None:
                print(f"URL [{urls[i]}]: {result}")
            else:
                print(f"URL [{urls[i]}] returned None.")

if __name__ == "__main__":
    asyncio.run(main())
