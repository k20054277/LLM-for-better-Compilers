import asyncio

async def fetch_data(url):
    # This function simulates a long-running task by sleeping for 2 seconds
    await asyncio.sleep(2)
    return 'Data from URL: {}'.format(url)

async def main():
    urls = ['http://www.example1.com', 'http://www.example2.com']
    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()