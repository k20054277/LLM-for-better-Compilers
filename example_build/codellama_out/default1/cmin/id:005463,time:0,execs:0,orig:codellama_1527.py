import asyncio

async def main():
    x = 10
    y = 3
    result = await asyncio.gather(divmod(x, y))
    print(result)

asyncio.run(main())