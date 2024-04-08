import asyncio

async def get_data(url):
    # Fetch data from URL
    data = await fetch(url)
    return data

async def main():
    urls = ["https://example.com", "https://example2.com"]
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_data(url))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())