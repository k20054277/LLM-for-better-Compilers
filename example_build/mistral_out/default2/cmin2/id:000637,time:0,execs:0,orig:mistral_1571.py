
import asyncio

# Define a coroutine that performs some I/O-bound task and yields a result.
async def mock_task(index):
    await asyncio.sleep(index)  # Simulate I/O operation taking index * sec seconds.
    return index * 2

# Create an asynchronous enumerator using async iterators and enumerate.
async def async_enumerate(iterable):
    async for index, item in enumerate(iterable, start=1):
        yield index, item

# Run the tasks concurrently in a single event loop.
async def main():
    tasks = [mock_task(i) for i in range(5)]
    enumerator = async_enumerate(tasks)

    results = await asyncio.gather(*enumerator)

    # Print the index and result of each task as it completes.
    for index, result in results:
        print(f"Task {index} completed with result: {result}")

# Run the main function in an event loop.
if __name__ == "__main__":
    asyncio.run(main())
