import asyncio

async def my_function(x, y):
    if x > 0 and y > 0:
        return x + y
    else:
        return None

async def main():
    print(await my_function(1, 2))  # Output: 3
    print(await my_function(-1, -2))  # Output: None

asyncio.run(main())