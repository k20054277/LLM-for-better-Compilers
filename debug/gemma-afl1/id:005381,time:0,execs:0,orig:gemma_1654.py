
import asyncio

async def hello(name):
    print("Hello, ", name)
    await asyncio.sleep(1)
    print("Goodbye, ", name)

# Create a list of coroutines
coros = [hello(i) for i in ["Alice", "Bob", "Charlie"]]

# Run the coroutines in parallel
await asyncio.gather(*coros)

print("All coroutines have completed")
