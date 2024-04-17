import asyncio

async def main():
    # Create a task using the async function 'do_something'
    task = asyncio.create_task(do_something())

    # Use the lambda function to print a message after 5 seconds
    asyncio.get_event_loop().call_later(5, lambda: print("Message printed after 5 seconds"))

    # Wait for both tasks to complete
    await task
    await asyncio.sleep(1)

async def do_something():
    # Do some work here
    pass

asyncio.run(main())