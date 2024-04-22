import asyncio

async def some_function():
    print("Starting...")
    await asyncio.sleep(2)
    print("Finished.")

loop = asyncio.get_event_loop()
task = loop.create_task(some_function())
while True:
    if task.done():
        break