
import asyncio

# Function that returns None and can be awaited in an asynchronous context
async def none_function():
    print("None function started")
    await asyncio.sleep(1)  # Simulate some work
    return None

# Function that prints a message and returns a string
async def print_message(message):
    print(f"Print message: {message}")
    return message

# Main function, demonstrates using None and async
async def main():
    none_result = await none_function()
    print("None result:", none_result)

    message = "Hello World!"
    message_result = await print_message(message)
    print("Message result:", message_result)

# Run the main function in an event loop
asyncio.run(main())
