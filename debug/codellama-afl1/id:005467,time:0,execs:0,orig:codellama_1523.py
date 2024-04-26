import asyncio
from math import sqrt

async def get_square_root(n):
    return await asyncio.create_task(sqrt(n))

async def main():
    # Create a list of numbers to calculate the square root for
    numbers = [1, 4, 9, 16, 25]
    
    # Use the async function to get the square roots asynchronously
    results = await asyncio.gather(*[get_square_root(n) for n in numbers])
    
    # Print the results
    print(results)

asyncio.run(main())