
import asyncio

async def my_async_function():
    try:
        # Simulate an asynchronous operation
        await asyncio.sleep(2)
    except Exception as e:
        # Raise an exception asynchronously
        raise e

async def main():
    # Create an asynchronous context
    await asyncio.gather(my_async_function(), return_exceptions=True)

    # Print the exceptions
    for e in main.exceptions:
        print(e)

asyncio.run(main())
