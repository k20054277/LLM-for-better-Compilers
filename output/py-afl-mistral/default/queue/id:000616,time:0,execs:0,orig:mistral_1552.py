
import asyncio
import aiohttp

async def fetch(url):
    """An asynchronous function to fetch web content."""
    async with aiohttp.Client() as client:
        async with client.get(url) as response:
            content = await response.text()
            return content

async def main():
    """The entry point of the script."""
    urls = [
        "https://example.com",
        "https://another-example.com",
        "https://third-example.com",
    ]

    tasks = []

    for url in urls:
        task = asyncio.create_task(fetch(url))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)

    for idx, response in enumerate(responses):
        print(f"Response from {urls[idx]}:\n{response}")

if __name__ == "__main__":
    asyncio.run(main())
