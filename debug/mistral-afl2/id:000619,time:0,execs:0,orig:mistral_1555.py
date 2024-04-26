
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            print(f'Error: {response.status} : {await response.reason()}')
            return None

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch(session, 'https://www.example1.com'),
            fetch(session, 'https://www.example2.com'),
            fetch(session, 'https://www.example3.com')
        ]

        results = await asyncio.gather(*tasks)
        
        print('Results:')
        for i, result in enumerate(results):
            if result is not None:
                print(f'{i+1}: {result}')
            else:
                print(f'{i+1}: Failed')

if __name__ == '__main__':
    asyncio.run(main())
