
import asyncio

async def fetch_data(i):
    # Simulate some asynchronous data fetching
    await asyncio.sleep(i)
    return i

async def main():
    # Create a list of tasks
    tasks = [fetch_data(i) for i in range(10)]

    # Use slice to slice the tasks and await them in parallel
    results = await asyncio.gather(*tasks[0:5])

    # Print the results
    print(results)

asyncio.run(main())
