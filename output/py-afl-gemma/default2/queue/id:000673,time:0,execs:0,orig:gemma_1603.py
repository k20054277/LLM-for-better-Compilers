
import asyncio

async def complex_task(n):
    # Simulate a complex task, such as fetching data from an API
    await asyncio.sleep(n)
    return n * 2

async def main():
    # Create a list of coroutines
    coroutines = [complex_task(i) for i in range(10)]

    # Run the coroutines in parallel
    results = await asyncio.gather(*coroutines)

    # Print the results
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
