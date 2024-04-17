
import asyncio
import aiohttp

async def download(session, url):
    async with session.get(url) as response:
        data = await response.text()
        return data

async def main():
    urls = ['https://example.com', 'https://anotherexample.com']
    async with aiohttp.ClientSession() as session:
        tasks = [download(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

        for response, url in zip(responses, urls):
            print(f'URL: {url}, Data length: {len(response)}')

if __name__ == '__main__':
    asyncio.run(main())
