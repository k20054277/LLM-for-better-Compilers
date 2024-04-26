
import asyncio

async def hello(name):
    print(f"Hello, {name}")

async def main():
    # Create a list of tasks
    tasks = [hello(i) for i in ["Alice", "Bob", "Charlie"]]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    print("All tasks complete!")

asyncio.run(main())
