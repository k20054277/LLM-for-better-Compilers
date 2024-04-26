
import asyncio

async def my_function(n):
    # Simulate some asynchronous task
    await asyncio.sleep(n)
    return n

async def main():
    # Create a list of futures
    futures = [my_function(i) for i in range(10)]

    # Use max to find the maximum value of the futures
    max_value = max(futures)

    # Print the maximum value
    print(max_value)

asyncio.run(main())
