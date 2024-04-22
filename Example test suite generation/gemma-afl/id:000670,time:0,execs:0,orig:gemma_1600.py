
import asyncio
import chr

async def hello_world(name):
    print(f"Hello, {name}!")

async def main():
    await asyncio.gather(*[hello_world(i) for i in ["Alice", "Bob", "Charlie"]])

asyncio.run(main())
