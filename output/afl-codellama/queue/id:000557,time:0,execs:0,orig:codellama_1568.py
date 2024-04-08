import asyncio

async def fetch(url):
    # Fetch the URL using the aiohttp library
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        return response.json()

async def main():
    urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
    results = []
    for url in urls:
        result = await fetch(url)
        results.append(result)
    sorted_results = sorted(results, key=lambda x: x["timestamp"])
    print("Sorted Results:")
    for result in sorted_results:
        print(result)

asyncio.run(main())