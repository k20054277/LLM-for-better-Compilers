
import asyncio

async def hello(i):
    print(f"Hello, world! from task {i}")

async def main():
    # Create a list of tasks
    tasks = [hello(i) for i in range(10)]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    print("All tasks complete!")

asyncio.run(main())
