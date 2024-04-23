
import asyncio
import aiohttp

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            print(f"Downloaded {url}: {len(content)} bytes")
            return content

async def main():
    urls = [
        "https://example.com",
        "https://www.google.com",
        "https://www.github.com",
    ]

    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download(url)))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
