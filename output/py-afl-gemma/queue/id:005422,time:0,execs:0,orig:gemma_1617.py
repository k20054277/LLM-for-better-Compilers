
import asyncio

async def my_async_function(name):
    print("Hello, " + name)
    await asyncio.sleep(1)
    print("Goodbye, " + name)

# Define a list of tasks
tasks = [my_async_function(i) for i in ["Alice", "Bob", "Charlie"]]

# Wait for all tasks to complete
await asyncio.gather(*tasks)

print("All tasks completed!")
