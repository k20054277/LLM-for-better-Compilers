
import asyncio
import ascii

async def hello_world(name):
    print(ascii.asciichart(80))
    print(f"Hello, {name}!")
    await asyncio.sleep(1)

async def main():
    names = ["John", "Jane", "Jack"]
    await asyncio.gather(*[hello_world(name) for name in names])

asyncio.run(main())
