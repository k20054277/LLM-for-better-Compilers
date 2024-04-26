async def main():
    tasks = []
    for i in range(5):
        task = asyncio.create_task(coroutine())
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    print(results)

async def coroutine():
    return "Hello"

asyncio.run(main())