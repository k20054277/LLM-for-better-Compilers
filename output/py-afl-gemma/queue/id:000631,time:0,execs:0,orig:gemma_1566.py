
async def hello(name):
    print(f"Hello, {name}!")
    # The following line simulates an asynchronous operation
    await asyncio.sleep(1)
    print(f"Continuing the conversation with, {name}")

# Create a list of coroutines
coroutines = [hello(i) for i in ["Alice", "Bob", "Charlie"]]

# Run the coroutines in parallel
await asyncio.gather(*coroutines)

# Print the results
print("All coroutines have completed")
