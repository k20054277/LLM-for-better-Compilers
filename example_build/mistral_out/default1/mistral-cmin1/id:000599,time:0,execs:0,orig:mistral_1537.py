
import asyncio
import aiohttp

async def fetch(url):
    """Asynchronously fetches a webpage."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            return data

async def scrape_websites(urls):
    """Scrapes multiple websites asynchronously."""
    tasks = [asyncio.create_task(fetch(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    return dict(zip(urls, results))

if __name__ == "__main__":
    urls = ["https://www.google.com", "https://www.github.com"]
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(scrape_websites(urls))
    print("Results:")
    for url, content in result.items():
        print(f"{url}: {len(content)} bytes")
