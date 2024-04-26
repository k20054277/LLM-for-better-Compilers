import asyncio
from math import sqrt

async def find_min(numbers):
    return min(numbers)

numbers = [1, 2, 3, 4, 5]

# Use async to call the function and get the result
result = await asyncio.create_task(find_min(numbers))
print(result) # Output: