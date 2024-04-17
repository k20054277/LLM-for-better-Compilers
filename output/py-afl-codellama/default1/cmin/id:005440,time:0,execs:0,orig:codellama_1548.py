import asyncio

async def my_function(x, y):
    # Use 'locals' to capture the current scope
    locals = {}
    async with asyncio.create_task(asyncio.sleep(1)) as task:
        await task
        result = x + y
        return result

print(my_function(2, 3))