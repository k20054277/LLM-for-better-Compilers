
import asyncio

async def hello(name):
    print(f"Hello, {name}")
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(*[hello(i) for i in ["Alice", "Bob", "Charlie"]])

asyncio.run(main())
