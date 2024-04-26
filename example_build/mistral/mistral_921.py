
import asyncio

# Function representing an independent task (coroutine)
async def task_a():
    print("Task A started")
    await asyncio.sleep(1)
    print("Task A completed")

async def task_b():
    print("Task B started")
    await asyncio.sleep(2)
    print("Task B completed")

# Main function
async def main():
    # Create the tasks
    task_a = asyncio.create_task(task_a())
    task_b = asyncio.create_task(task_b())

    # Wait for both tasks to complete using 'and' operator
    await asyncio.wait([task_a, task_b])

    print("Both tasks completed")

# Run the main function
asyncio.run(main())
