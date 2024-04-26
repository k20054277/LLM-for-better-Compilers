
import asyncio

async def hello(name):
    print(f"Hello, {name}!")

async def main():
    names = ["John", "Jane", "Jack"]
    results = [hello(name) for name in names]

    # Use any to check if any result is successful
    if any(result.is_completed() for result in results):
        print("At least one hello was successful!")

    # Wait for all results to complete
    await asyncio.gather(*results)

    print("All hellos have completed!")

asyncio.run(main())
