import asyncio

async def fetch_data(url):
    # Fetch data from the URL using the aiohttp library
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.read()
    return data

# Use the fetch_data function to fetch some data
async def main():
    url = "https://www.example.com"
    data = await fetch_data(url)
    # Do something with the data
    print(data)

asyncio.run(main())