import asyncio

async def greet(name):
    print(f"Hello, {name}!")

# Using the 'global' keyword to make the variable 'name' accessible from all functions
global name

async def main():
    # Setting the value of the global variable 'name'
    name = "Alice"
    
    # Starting the coroutine asynchronously
    await greet(name)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())