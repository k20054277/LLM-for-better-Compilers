
import asyncio

async def hello_world():
    print("Hello, world!")
    return 4.5

async def main():
    print(await hello_world())

asyncio.run(main())
