
import asyncio

async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)  # Simulate a delay

async def main():
    # Create a list of coroutines
    coros = [greet(i) for i in ["Alice", "Bob", "Charlie"]]

    # Run the coroutines in parallel
    await asyncio.gather(*coros)

    print("All greetings have been completed!")

asyncio.run(main())
