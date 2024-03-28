
import asyncio

async def my_async_function(n):
    print(n)
    await asyncio.sleep(1)

async def main():
    # Create a list of tasks
    tasks = [my_async_function(i) for i in range(10)]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    print("All tasks completed!")

asyncio.run(main())
