
import asyncio
import random

# Define an asynchronous function to generate a random number
async def generate_number():
    return random.randint(1, 10)

# Map over a list of 100 tasks to generate random numbers asynchronously
numbers_task = [generate_number() for _ in range(100)]

# Use asyncio.gather to wait for all tasks to complete
numbers_result = await asyncio.gather(*numbers_task)

# Print the results
print(numbers_result)
