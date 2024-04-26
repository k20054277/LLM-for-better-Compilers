import asyncio

async def my_coroutine():
    await asyncio.sleep(1)  # simulate a long-running task
    return True

async def main():
    result = await my_coroutine()
    print(result)  # prints "True"

asyncio.run(main())