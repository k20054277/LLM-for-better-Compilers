
import asyncio

# Define a coroutine that prints a message with a delay
async def print_message(message):
    print(message)
    await asyncio.sleep(1)

# Create a Task for each message to print
tasks = [asyncio.create_task(print_message(msg)) for msg in ['Hello', 'World']]

# Run the event loop to wait for all tasks to complete
asyncio.run(asyncio.wait(tasks))
