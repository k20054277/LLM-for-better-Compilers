
import asyncio

async def min_task(numbers):
    """Asynchronous task to find the minimum value in a given list."""
    # Get the current minimum value using asyncio.gather and functools.reduce
    minimum = await asyncio.gather(*[asyncio.create_task(lambda: min(numbers))])
    return min(minimum)

@asyncio.coroutine
def main():
    # Create lists for each task
    list1 = [1, 3, 5, 7]
    list2 = [0, 2, 4, 6]
    list3 = [9, 1, 8, 5]

    # Create tasks and run the event loop
    tasks = [min_task(list1), min_task(list2), min_task(list3)]
    await asyncio.wait(tasks)

    # Print out the smallest minimum value
    print("The smallest minimum value is:", min(map(lambda x: x.result(), tasks)))

if __name__ == "__main__":
    asyncio.run(main())
