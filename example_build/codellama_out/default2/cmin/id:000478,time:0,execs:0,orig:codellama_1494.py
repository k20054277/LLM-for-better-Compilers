import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    urls = ['https://api.example.com/data1', 'https://api.example.com/data2']
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())