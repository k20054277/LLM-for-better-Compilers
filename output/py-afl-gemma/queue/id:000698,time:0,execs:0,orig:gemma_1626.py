
import asyncio

async def fetch_data(url):
    # Simulate fetching data asynchronously
    await asyncio.sleep(1)
    return url + " data"

async def main():
    # Create an asynchronous iterator
    async iter = iter(lambda: fetch_data(str(i) for i in range(1, 11)), None)

    # Iterate over the asynchronous iterator
    for data in async iter:
        print(data)

asyncio.run(main())
