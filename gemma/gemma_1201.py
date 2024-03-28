
import asyncio

async def hello(name):
    print("Hello, ", name)

async def main():
    # Create a list of coroutines
    coros = [hello(i) for i in ["Alice", "Bob", "Charlie"]]

    # Run the coroutines concurrently
    await asyncio.gather(*coros)

    print("All coroutines completed")

asyncio.run(main())
