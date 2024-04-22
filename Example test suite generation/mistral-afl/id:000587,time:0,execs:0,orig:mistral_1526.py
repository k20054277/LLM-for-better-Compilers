
import asyncio
import aiohttp

async def download(url):
    """Download function that uses async and await"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            print(f'Downloaded {url} with status code: {response.status}')
            return content

async def main():
    """Main function for the script"""
    urls = ['https://example.com', 'https://www.example.org', 'https://www.example.net']
    tasks = [download(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
