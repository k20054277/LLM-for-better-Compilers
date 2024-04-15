
import asyncio

# This is the other module, let's assume it's called 'my_module.py'
# and is located in the same directory as this file
async def fetch_data():
    # Import the my_function function from 'my_module'
    import my_module

    # Call the my_function asynchronously
    result = await asyncio.get_event_loop().run_in_executor(None, my_module.my_function)
    
    print("Result: ", result)

if __name__ == "__main__":
    asyncio.run(fetch_data())
