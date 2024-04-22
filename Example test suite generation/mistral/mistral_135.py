
import asyncio

# A simple coroutine function that waits for seconds and prints a message.
async def print_message(message: str, seconds: float):
    await asyncio.sleep(seconds)  # Wait for the specified number of seconds.
    print(message)

# Create tasks and run them concurrently using asyncio.
async def main():
    task1 = asyncio.create_task(print_message("Task 1", 2))
    task2 = asyncio.create_task(print_message("Task 2", 3))
    
    await asyncio.gather(*[task1, task2])  # Wait for all tasks to complete.

if __name__ == "__main__":
    asyncio.run(main())
