
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                return data
            else:
                raise Exception(f'Error fetching URL: {url}')

async def main():
    urls = ['https://www.example1.com', 'https://www.example2.com']
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(fetch(url)))
    responses = await asyncio.gather(*tasks)

    print('Responses:')
    for i, response in enumerate(responses):
        print(f'URL [{i}]: {response}')

if __name__ == '__main__':
    asyncio.run(main())
