
import asyncio

async def hello_world():
    print("Hello, world!")

async def main():
    await hello_world()
    print("Goodbye, world!")

asyncio.run(main())
