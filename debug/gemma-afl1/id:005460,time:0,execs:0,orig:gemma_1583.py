
import asyncio

async def hello_world():
    print("Hello, world!")

async def main():
    # Run the hello_world function asynchronously
    await hello_world()

    # Continue the main loop
    print("Continuing...")

asyncio.run(main())
