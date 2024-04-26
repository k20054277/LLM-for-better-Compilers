
import asyncio
import aiohttp

async def fetch_number(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data['number']

async def get_max_number(numbers):
    max_number = max(numbers)
    return max_number

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['http://example.com/number1', 'http://example.com/number2']
        tasks = [asyncio.create_task(fetch_number(session, url)) for url in urls]
        numbers = await asyncio.gather(*tasks)
        max_number = await get_max_number(numbers)
        print('The maximum number is:', max_number)

if __name__ == '__main__':
    asyncio.run(main())
