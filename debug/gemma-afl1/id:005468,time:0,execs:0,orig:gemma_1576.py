
import asyncio

async def hello(name):
    print(f"Hello, {name}")

async def main():
    # Create a list of coroutines
    coroutines = [hello(i) for i in ["Alice", "Bob", "Charlie"]]

    # Run the coroutines in parallel
    await asyncio.gather(*coroutines)

    print("All coroutines have completed")

asyncio.run(main())
