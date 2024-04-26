
import asyncio

async def hello(name):
    print(f"Hello, {name}")

async def main():
    # Create a list of tasks
    tasks = [hello(i) for i in range(10)]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    print("All tasks completed")

asyncio.run(main())
