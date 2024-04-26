
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            return data

async def scrape_websites(urls):
    tasks = [fetch(url) for url in urls]
    responses = await asyncio.gather(*tasks)

    for i, (url, response) in enumerate(zip(urls, responses)):
        print(f"URL: {url}\nResponse length: {len(response)}")
        print(response)

if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://www.google.com",
        "https://stackoverflow.com"
    ]
    asyncio.run(scrape_websites(urls))
