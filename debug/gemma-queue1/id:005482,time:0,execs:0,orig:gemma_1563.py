
# Define an asynchronous function
async def hello_world():
    # Simulate some asynchronous operation, like fetching data from an API
    await asyncio.sleep(2)
    return "Hello, world!"

# Define a main function
async def main():
    # Create an asynchronous context
    async with asyncio.get_event_loop() as loop:
        # Run the asynchronous function
        result = await hello_world()

    # Print the result
    print(result)

# Execute the main function
asyncio.run(main())
