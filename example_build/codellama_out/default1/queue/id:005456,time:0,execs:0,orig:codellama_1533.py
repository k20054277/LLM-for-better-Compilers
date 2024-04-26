import asyncio

async def get_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

urls = ["https://api.example.com/users", "https://api.example.com/posts"]

results = []
for url in urls:
    results.append(asyncio.create_task(get_data(url)))

await asyncio.gather(*results)

for result in results:
    print(result)