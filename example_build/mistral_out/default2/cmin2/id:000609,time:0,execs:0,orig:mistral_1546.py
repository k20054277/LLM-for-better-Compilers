
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        if response.status in (200, 304):
            return await response.text()
        else:
            raise Exception('Request failed: ' + response.status_text)

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com', 'https://anotherexample.com']
        tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
        response1 = await tasks[0]
        response2 = await tasks[1] or ''

        print('Response from first URL:')
        print(response1)
        print('Response from second URL (or empty string if failed):')
        print(response2)

if __name__ == '__main__':
    asyncio.run(main())
