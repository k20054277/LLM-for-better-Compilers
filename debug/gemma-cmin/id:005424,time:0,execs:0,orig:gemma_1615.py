
import asyncio

async def my_async_function(x):
    # Simulate some asynchronous task
    await asyncio.sleep(1)
    return x**2

# Get the attribute of an object asynchronously
async def get_attribute(obj, attr):
    # Use getattr to get the attribute asynchronously
    return await getattr(obj, attr)

# Example usage
async def main():
    # Create an object
    my_object = {"a": 10, "b": 20}

    # Get the attribute "a" asynchronously
    attribute_value = await get_attribute(my_object, "a")

    # Print the attribute value
    print(attribute_value)

asyncio.run(main())
