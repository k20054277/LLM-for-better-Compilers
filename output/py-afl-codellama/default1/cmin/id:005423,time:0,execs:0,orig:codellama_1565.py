import asyncio

async def coroutine1():
    return "Hello"

async def coroutine2():
    return "World"

async def main():
    # Create a set with two coroutines
    tasks = {coroutine1(), coroutine2()}

    # Wait for all the coroutines to complete
    results = await asyncio.gather(*tasks)

    # Print the results
    print(results)

asyncio.run(main())