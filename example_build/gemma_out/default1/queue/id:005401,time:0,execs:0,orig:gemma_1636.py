
import asyncio
import oct

async def hello_world():
    print("Hello, world!")

async def main():
    await hello_world()
    print("Main completed")

asyncio.run(main())
