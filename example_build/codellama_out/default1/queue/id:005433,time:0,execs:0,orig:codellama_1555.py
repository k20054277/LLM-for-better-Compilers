import asyncio

async def my_coroutine():
    print("Hello from my coroutine!")
    await asyncio.sleep(1)
    print("I'm done sleeping for now.")

async def main():
    task = asyncio.create_task(my_coroutine())
    result = await task
    print(result)

if __name__ == '__main__':
    asyncio.run(main())