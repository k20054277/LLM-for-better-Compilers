
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, "https://example.com/1"), fetch(session, "https://example.com/2")]
        results = await asyncio.gather(*tasks)

        print("Results:")
        for i, result in enumerate(results):
            print(f"Result {i + 1}: {result}")

if __name__ == "__main__":
    asyncio.run(main())
