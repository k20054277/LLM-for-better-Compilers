from concurrent.futures import ThreadPoolExecutor
import asyncio

async def fetch_data(url):
    print("Fetching data from {}".format(url))
    await asyncio.sleep(1)
    return "Data from {}".format(url)

async def main():
    url = ["https://example.com", "https://example2.com"]
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [executor.submit(fetch_data, url) for url in url]
        responses = await asyncio.gather(*tasks)
        print("Responses: {}".format(responses))

asyncio.run(main())