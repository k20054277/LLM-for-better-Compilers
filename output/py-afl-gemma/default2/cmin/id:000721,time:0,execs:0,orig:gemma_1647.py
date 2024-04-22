
import asyncio

async def my_async_function(name):
    print(f"Hello, {name}")
    await asyncio.sleep(1)
    setattr(globals(), name, 10)

async def main():
    await asyncio.gather(*[my_async_function(i) for i in ["Alice", "Bob", "Charlie"]])
    print(globals())

asyncio.run(main())
