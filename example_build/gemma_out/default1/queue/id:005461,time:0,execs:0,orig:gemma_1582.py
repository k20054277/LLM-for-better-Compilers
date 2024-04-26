
import asyncio

# Async function
async def hello_async(name):
    print("Hello, ", name)
    await asyncio.sleep(1)
    print("Async function finished")

# Non-async function
def hello_non_async(name):
    print("Hello, ", name)
    time.sleep(1)
    print("Non-async function finished")

# Main event loop
asyncio.run(hello_async("Alice"))
asyncio.run(hello_non_async("Bob"))

print("Both functions finished")
