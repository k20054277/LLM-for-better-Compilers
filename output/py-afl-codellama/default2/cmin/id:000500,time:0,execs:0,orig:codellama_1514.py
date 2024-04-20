import asyncio

async def main():
    # Asynchronous function that sleeps for 1 second
    await asyncio.sleep(1)

    # Print a message using ASCII characters
    print("Hello, world!")

asyncio.run(main())