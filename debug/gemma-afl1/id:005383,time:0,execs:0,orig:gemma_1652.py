
import asyncio

async def fetch_number(n):
    # Simulate some async operation, like fetching a number from an API
    await asyncio.sleep(n)
    return n

async def main():
    # Create a list of tasks
    tasks = [fetch_number(i) for i in range(10)]

    # Use asyncio.gather to wait for all tasks to complete
    results = await asyncio.gather(*tasks)

    # Print the results
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
