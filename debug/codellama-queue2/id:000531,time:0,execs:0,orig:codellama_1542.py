import asyncio

async def fetch_data(url):
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
    return response.json()

async def main():
    urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
    results = await asyncio.gather(*[fetch_data(url) for url in urls])
    print(results)

asyncio.run(main())