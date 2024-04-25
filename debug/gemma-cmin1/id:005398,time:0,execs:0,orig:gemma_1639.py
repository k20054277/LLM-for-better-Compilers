
import asyncio

async def square(x):
    await asyncio.sleep(1)  # Simulate some delay
    return x ** 2

async def main():
    # Create a list of futures
    futures = [square(i) for i in range(1, 4)]

    # Wait for all futures to complete
    results = await asyncio.gather(*futures)

    # Print the results
    print(results)

asyncio.run(main())
