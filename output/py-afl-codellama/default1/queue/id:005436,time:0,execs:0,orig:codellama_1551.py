import asyncio
import numpy as np

async def main():
    # Create an array of integers
    arr = np.array([1, 2, 3, 4, 5])

    # Use memoryview to create a view of the array
    mv = memoryview(arr)

    # Print the length of the view
    print(len(mv))

    # Modify the elements in the view
    mv[0] = 10
    mv[2] = 20

    # Print the updated array
    print(arr)

asyncio.run(main())