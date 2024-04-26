import asyncio

async def main():
    print(f"The current coroutine ID is {id(asyncio.current_task())}")

asyncio.run(main())