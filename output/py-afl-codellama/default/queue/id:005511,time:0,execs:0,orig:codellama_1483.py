import asyncio

async def fetch_data(url):
    response = await asyncio.create_task(requests.get(url))
    return response.json()

async def main():
    urls = ['http://example.com/data1', 'http://example.com/data2']
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

asyncio.run(main())