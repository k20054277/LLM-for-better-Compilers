
import asyncio

async def my_async_function(n):
    print(n)
    await asyncio.sleep(1)
    print(n * 2)

async def main():
    await asyncio.gather(*[my_async_function(i) for i in range(5)])

asyncio.run(main())
