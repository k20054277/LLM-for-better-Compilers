import asyncio

async def get_data(url):
    print("Starting to fetch data from", url)
    # Fake a long-running task
    await asyncio.sleep(3)
    return "Data from {}".format(url)

async def main():
    tasks = []
    for i in range(5):
        tasks.append(get_data("https://example.com/{}".format(i)))
    results = await asyncio.gather(*tasks)
    print("Data fetched:", ", ".join(results))

asyncio.run(main())