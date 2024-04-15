
import asyncio

async def my_async_function(n):
    # Simulate some asynchronous task
    await asyncio.sleep(n)
    return n

async def main():
    # Define a list of futures
    futures = [my_async_function(i) for i in range(5)]

    # Use await to wait for all futures to complete
    results = await asyncio.gather(*futures)

    # Print the results
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
