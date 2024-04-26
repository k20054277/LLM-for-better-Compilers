
import asyncio
import aiohttp

async def fetch(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"Error: Server returned status code {response.status}")
                data = await response.text()
                return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

async def main():
    urls = ["http://example.com", "http://nonexistent.com"]
    tasks = [asyncio.create_task(fetch(url)) for url in urls]
    results = await asyncio.gather(*tasks)

    for i, result in enumerate(results):
        print(f"URL #{i+1} result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
