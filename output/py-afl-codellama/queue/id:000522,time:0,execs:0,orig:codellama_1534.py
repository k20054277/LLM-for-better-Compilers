import asyncio

async def my_coroutine():
    return frozenset([1, 2, 3])

async def main():
    result = await my_coroutine()
    print(result)

asyncio.run(main())