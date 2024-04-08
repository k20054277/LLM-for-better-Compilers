import asyncio

async def my_function(x):
    if x > 0:
        return True
    else:
        return False

async def main():
    result = await my_function(1)
    print(result)

asyncio.run(main())