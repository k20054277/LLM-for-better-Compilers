
import asyncio
import aiohttp
import json

async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Error: URL returned status code {response.status}")
            return await response.json()
    except aiohttp.ClientError as e:
        print(f"Exception in fetch_url for url '{url}': {e}")
        return None

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, "http://example1.com"), fetch_url(session, "http://example2.com")]
        results = await asyncio.gather(*tasks)

        print("Results:")
        for i, result in enumerate(results):
            if result is not None:
                print(f"URL {i+1}: {json.dumps(result)}")

if __name__ == "__main__":
    asyncio.run(main())
