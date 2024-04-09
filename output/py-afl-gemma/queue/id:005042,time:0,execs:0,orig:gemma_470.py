
import asyncio

# Define a function that returns None
async def none_function():
    return None

# Define a function that returns a future with None
async def future_none(delay):
    await asyncio.sleep(delay)
    return None

# Create a list of tasks
tasks = [none_function(), future_none(2), future_none(3)]

# Wait for all tasks to complete
await asyncio.gather(*tasks)

# Print the results of the tasks
print("Results:")
for task in tasks:
    print(task.result())
