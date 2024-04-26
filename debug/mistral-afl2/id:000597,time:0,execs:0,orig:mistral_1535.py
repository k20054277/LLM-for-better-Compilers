
import asyncio
import aiohttp

async def send_request(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.text()
                print(f'Response from {url}:')
                print(data)
    except Exception as e:
        print(f'Error: {e}')
        await asyncio.sleep(1)  # wait for a second before exiting the coroutine

@asyncio.coroutine
def main():
    urls = ['http://example.com', 'http://non-existing-url']
    tasks = [asyncio.ensure_future(send_request(url)) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
