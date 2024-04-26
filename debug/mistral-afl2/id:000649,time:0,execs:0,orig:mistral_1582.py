
import asyncio
import aiohttp

async def fetch(url):
    """Asynchronously fetch URL."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    """Fetch the content of multiple URLs concurrently."""
    urls = [
        "https://example.com",
        "https://another-example.com",
        "https://yet-another-example.com"
    ]

    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(url))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)

    print("Responses:")
    for response, url in zip(responses, urls):
        print(f"URL: {url}\nResponse: {response}\n------------------------")

if __name__ == "__main__":
    asyncio.run(main())
