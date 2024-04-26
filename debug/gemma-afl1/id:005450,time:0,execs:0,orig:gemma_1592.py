
import asyncio

async def hello(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)
    print(f"Hello, {name}! Again!")

async def main():
    await asyncio.gather(*[hello(name) for name in ["Alice", "Bob", "Charlie"]])

asyncio.run(main())
