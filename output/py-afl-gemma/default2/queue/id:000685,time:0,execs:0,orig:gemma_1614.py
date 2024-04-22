
import asyncio

# Define a frozenset of numbers
numbers_frozenset = frozenset([1, 2, 3, 4, 5])

# Define an asynchronous function
async def print_numbers(numbers_frozenset):
    for number in numbers_frozenset:
        print(number)

# Create an asynchronous event loop
event_loop = asyncio.get_event_loop()

# Run the asynchronous function
await print_numbers(numbers_frozenset)

# Close the event loop
event_loop.close()
