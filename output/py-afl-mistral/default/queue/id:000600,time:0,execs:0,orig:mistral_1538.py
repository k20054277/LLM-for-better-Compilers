
import asyncio

# This function is marked as async, meaning it can yield control to other tasks
async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)

# The main function is marked as async as well and uses the run_until_complete() method to start the coroutine
async def main():
    await print_numbers()

if __name__ == "__main__":
    asyncio.run(main())
