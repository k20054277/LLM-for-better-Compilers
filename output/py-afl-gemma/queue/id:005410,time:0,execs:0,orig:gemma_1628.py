
import asyncio

async def hello(name):
    print(f"Hello, {name}")

async def main():
    # Create a list of coroutines
    coros = [hello(i) for i in ["Alice", "Bob", "Charlie"]]

    # Run the coroutines in parallel
    await asyncio.gather(*coros)

    print("All coroutines have finished")

asyncio.run(main())
