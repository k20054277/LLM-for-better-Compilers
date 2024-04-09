
import asyncio

async def my_coroutine(n):
    print("Coroutine", n)
    await asyncio.sleep(1)
    return n * 2

async def main():
    # Create a list of coroutines
    coroutines = [my_coroutine(i) for i in range(5)]

    # Run the coroutines in parallel
    results = await asyncio.gather(*coroutines)

    # Print the results
    print("Results:", results)

asyncio.run(main())
