import asyncio

async def async_function():
    return 10.5

def main():
    result = await async_function()
    print(result)

asyncio.run(main())