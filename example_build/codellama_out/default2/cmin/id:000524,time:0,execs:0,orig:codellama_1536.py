import asyncio

async def foo(x):
    global y
    y = x * 2
    await asyncio.sleep(1)
    return y

async def main():
    y = None
    task = asyncio.create_task(foo(5))
    await task
    print(y)

asyncio.run(main())