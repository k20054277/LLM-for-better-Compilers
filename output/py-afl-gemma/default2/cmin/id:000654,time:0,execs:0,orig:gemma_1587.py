
import asyncio

async def my_async_function():
    try:
        # Perform some asynchronous operation, such as fetching data from a server
        await asyncio.sleep(2)
        return "Success!"
    except Exception as e:
        # Handle any exceptions that occur during the asynchronous operation
        return "Error: {}".format(e)

# Run the asynchronous function and handle the result
result = asyncio.run(my_async_function())

# Print the result
print(result)
