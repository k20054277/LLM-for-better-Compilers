
import asyncio

async def my_async_function(x):
    print("Hello, world!", x)
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(*[my_async_function(i) for i in range(5)])

asyncio.run(main())
