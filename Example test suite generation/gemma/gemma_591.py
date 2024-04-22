
# True and Await Example

import asyncio

async def hello_world():
    print("Hello, world!")
    return True

async def main():
    await hello_world()
    print("The program continues...")

asyncio.run(main())
