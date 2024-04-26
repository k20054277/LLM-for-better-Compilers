
import asyncio

async def hello_world(name):
    print(f"Hello, {name}!")

async def main():
    # Create a list of coroutines
    coroutines = [hello_world(i) for i in ["Alice", "Bob", "Charlie"]]

    # Run the coroutines in parallel
    await asyncio.gather(*coroutines)

    print("All coroutines completed!")

asyncio.run(main())
