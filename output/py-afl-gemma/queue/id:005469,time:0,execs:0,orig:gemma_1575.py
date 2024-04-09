
import asyncio

# Define a global variable
global_variable = 10

# Define an asynchronous function
async def asynchronous_function():
    print("Asynchronous function started")
    await asyncio.sleep(2)
    print("Asynchronous function completed")

# Define an asynchronous coroutine
async def asynchronous_coroutine():
    print("Asynchronous coroutine started")
    await asyncio.sleep(2)
    print("Asynchronous coroutine completed")

# Run the event loop
asyncio.run(asyncio.gather(asynchronous_function(), asynchronous_coroutine()))

# Print the global variable
print("Global variable:", global_variable)
