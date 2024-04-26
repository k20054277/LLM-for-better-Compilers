
import asyncio

# Define a function that prints a message and returns False
async def print_message(message):
    print(message)
    return False

# Create an asyncio event loop
event_loop = asyncio.get_event_loop()

# Create a list of coroutines
coroutines = [print_message("Hello, world!") for _ in range(5)]

# Run the coroutines concurrently
await asyncio.gather(*coroutines)

# Print a message after all coroutines have completed
print("All coroutines completed")
