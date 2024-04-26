
import asyncio

# Define a function that returns a coroutine
async def hello_world():
    print("Hello, world!")
    return

# Use False to check if the coroutine is ready
if False:
    await hello_world()

# Use await to wait for the coroutine to complete
await hello_world()

print("The coroutine has completed")
