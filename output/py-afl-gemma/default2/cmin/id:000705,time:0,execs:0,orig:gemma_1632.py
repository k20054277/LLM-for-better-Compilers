
import asyncio
import numpy as np

async def memory_view_async(size):
    # Create a memory view of the specified size
    arr = np.memview(np.uint32, size)

    # Fill the memory view with random numbers
    arr.fill(np.random.randint(1, 10, size))

    # Print the memory view
    print(arr)

asyncio.run(memory_view_async(10**4))
