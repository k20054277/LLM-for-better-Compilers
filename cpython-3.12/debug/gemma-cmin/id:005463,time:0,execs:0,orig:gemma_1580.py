
import asyncio

async def square(x):
    return x ** 2

async def main():
    # Create a list of tasks
    tasks = [square(i) for i in range(1, 6)]

    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)

    # Print the results
    print(results)

asyncio.run(main())
