from asyncio import async, reversed

async def foo():
    return 42

async def bar():
    return await reversed(foo())

print(await bar()) # prints