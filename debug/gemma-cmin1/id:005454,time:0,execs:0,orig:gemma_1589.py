
import asyncio

async def my_async_function(n):
    # Simulate some asynchronous operation
    await asyncio.sleep(n)
    print("Hello, world!", n)


async def main():
    # Use 'with' to manage the lifecycle of an asynchronous context
    async with asyncio.get_event_loop() as loop:
        # Create a list of tasks
        tasks = [my_async_function(i) for i in range(10)]

        # Wait for all tasks to complete
        await asyncio.gather(*tasks)

    print("All tasks completed")


if __name__ == "__main__":
    asyncio.run(main())
