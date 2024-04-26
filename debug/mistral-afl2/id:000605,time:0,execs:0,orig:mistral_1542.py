
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Fetched {url} with status code: {response.status}")

if __name__ == "__main__":
    urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.example.com"
    ]

    tasks = [asyncio.create_task(fetch(url)) for url in urls]

    await asyncio.gather(*tasks)
