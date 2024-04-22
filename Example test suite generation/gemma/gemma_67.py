
async def my_function():
    # Use await to get the result of an asynchronous function
    await print("Hello, world!")

# Use and to execute multiple asynchronous functions in parallel
async def main():
    my_function()
    print("Continuing with the main function...")

# Execute the main function
main()
