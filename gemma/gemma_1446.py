
import asyncio

async def my_coro():
    assert 10 == 10
    return "Hello, world!"

async def main():
    result = await my_coro()
    print(result)

asyncio.run(main())
