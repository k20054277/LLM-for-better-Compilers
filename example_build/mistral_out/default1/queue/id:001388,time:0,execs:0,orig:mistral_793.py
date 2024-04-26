
import asyncio
import aiohttp

async def fetch(url):
    """Asynchronously fetches a web page."""
    async with aiohttp.Client() as client:
        async with client.get(url) as response:
            if response.status in range(200, 300):
                return await response.text()
            else:
                print(f'Error fetching {url}: {response.status}')
                return None

async def main():
    urls = ['https://www.google.com', 'https://www.example.com', 'https://non-existent-url.com']

    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)

    # Check all fetches were successful and print results
    if all(result is not None for result in results):
        print('All fetch operations completed successfully!')
        print('Results:')
        for i, url in enumerate(urls):
            print(f'{i + 1}. {url}: {results[i]}')
    else:
        print('Error: Some fetch operations failed.')

if __name__ == '__main__':
    asyncio.run(main())
