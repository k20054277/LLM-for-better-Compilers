import asyncio

# Define a coroutine that returns False
async def my_coroutine():
    return False

# Use the coroutine with async/await syntax
async def main():
    result = await my_coroutine()
    print(result)  # This will print "False"

# Run the main function
asyncio.run(main())