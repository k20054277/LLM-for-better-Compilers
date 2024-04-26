
import asyncio

async def hello(name):
    print(f"Hello, {name}")

async def main():
    names = ["Alice", "Bob", "Charlie"]
    await asyncio.gather(*[hello(name) for name in names])

asyncio.run(main())
