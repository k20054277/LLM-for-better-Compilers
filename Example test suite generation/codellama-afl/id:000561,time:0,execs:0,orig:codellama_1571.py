import asyncio

async def sum(a, b):
    return a + b

async def main():
    result = await sum(2, 3)
    print(result)

asyncio.run(main())