import asyncio

async def async_function():
    # Do some asynchronous work here, such as making a network request or waiting on a coroutine.
    await asyncio.sleep(1)

# Use the `as` keyword to indicate that the function is an asynchronous function.
@asyncio.coroutine
def main():
    # Create a task for the asynchronous function.
    task = asyncio.create_task(async_function())

    # Wait for the task to complete.
    await task

# Run the `main` function.
if __name__ == '__main__':
    main()