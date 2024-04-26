
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            raise Exception(f"Error getting URL: {url}")

async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            "https://example.com",
            "https://another-example.com",
            "https://yet-another-example.com"
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
        results = await asyncio.gather(*tasks)

        print("Fetched URLs:")
        for idx, result in enumerate(results):
            print(f"URL #{idx + 1}: {result}")

if __name__ == "__main__":
    asyncio.run(main())
