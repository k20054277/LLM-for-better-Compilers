
import asyncio

# Define a global variable
global_variable = 10

# Define an asynchronous function
async def async_function():
    # Print the global variable
    print("Global variable:", global_variable)

    # Sleep for 2 seconds
    await asyncio.sleep(2)

    # Print the global variable again
    print("Global variable after sleep:", global_variable)

# Create an asynchronous event loop
asyncio.run(async_function())
