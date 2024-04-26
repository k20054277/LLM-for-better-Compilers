
import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            return data

async def main():
    urls = [
        "https://example.com",
        "https://another-example.com"
    ]

    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]

    results = await asyncio.gather(*tasks)

    print("Results:")
    for result, url in zip(results, urls):
        print(f"URL '{url}': {result}")

if __name__ == "__main__":
    asyncio.run(main())
