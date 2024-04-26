
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            return data

async def main():
    urls = ['https://example.com', 'https://example.org']
    tasks = [fetch(u) for u in urls]
    results = await asyncio.gather(*tasks)

    print('Results:')
    for i, r in enumerate(results):
        print(f'URL {i+1}: {r}')

if __name__ == '__main__':
    asyncio.run(main())
