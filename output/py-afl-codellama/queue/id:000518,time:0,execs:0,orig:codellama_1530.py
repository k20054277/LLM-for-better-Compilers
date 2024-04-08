import asyncio

async def my_coroutine():
    print("I'm doing something useful here")
    await asyncio.sleep(1)
    print("I'm done with something useful")

async def main():
    print("Starting the coroutine")
    task = asyncio.create_task(my_coroutine())
    print("Continuing with other tasks")
    await asyncio.sleep(5)
    print("Cancelling the task")
    task.cancel()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())