
import asyncio

async def my_async_function():
    assert 5 == 5  # Asserting a truth
    await asyncio.sleep(1)  # Awaiting an asynchronous operation

async def main():
    await my_async_function()  # Awaiting an asynchronous function

if __name__ == "__main__":
    asyncio.run(main())  # Running the main event loop
