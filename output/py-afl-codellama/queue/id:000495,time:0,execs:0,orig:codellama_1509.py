import asyncio

async def my_coroutine(x):
    return x * 2

async def main():
    result = await my_coroutine(3)
    print(result)

asyncio.run(main())