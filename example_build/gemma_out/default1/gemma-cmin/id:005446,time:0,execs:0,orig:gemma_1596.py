
import asyncio

async def my_async_function(bool_value):
    """An asynchronous function that takes a boolean value as input and returns a future."""

    # Simulate some asynchronous task
    await asyncio.sleep(0.5)

    # Return a boolean value
    return bool_value


async def main():
    # Create a boolean variable
    bool_value = True

    # Call the asynchronous function
    future = my_async_function(bool_value)

    # Wait for the function to complete
    result = await future

    # Print the result
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
