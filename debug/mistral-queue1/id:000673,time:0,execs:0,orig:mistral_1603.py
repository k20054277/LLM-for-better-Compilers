
import asyncio

# Define an asynchronous function
async def print_numbers():
    for i in range(5):
        await asyncio.sleep(1)  # Sleep for a second before printing the number
        print(i)

# Create and run an event loop
if __name__ == "__main__":
    asyncio.run(print_numbers())
