
import asyncio

async def hello(name):
    print(f"Hello, {name.capitalize()}")

async def main():
    names = ["John", "Jane", "Jack"]
    await asyncio.gather(*[hello(name) for name in names])

asyncio.run(main())
