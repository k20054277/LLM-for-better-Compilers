
import asyncio

async def hello_world():
    print("Hello, world!")

async def main():
    await hello_world()
    print(len(await hello_world()))

asyncio.run(main())
