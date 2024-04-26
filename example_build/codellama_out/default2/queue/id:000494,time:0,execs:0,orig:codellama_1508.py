import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://api.example.com/data')
        data = await response.json()
        print(data)

asyncio.run(main())