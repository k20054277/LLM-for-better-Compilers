
import asyncio

# Define a coroutine that prints a greeting message asynchronously
async def print_greeting(name):
    await asyncio.sleep(1)  # Simulate some work
    print(f"Hello, {name}!")

# Create a list of names and an event to signal the end of coroutines
names = ["Alice", "Bob", "Charlie"]
done_event = asyncio.Event()

# Create a task for each name using create_task() method
tasks = [asyncio.create_task(print_greeting(name)) for name in names]

# Wait for all tasks to complete using wait() method
await asyncio.gather(*tasks)
await done_event.wait()

# Print a message when all tasks are completed
print("All greetings sent!")
