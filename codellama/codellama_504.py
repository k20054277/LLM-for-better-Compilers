import asyncio

async def my_function(arg1, arg2):
    if arg1 is None:
        return None
    else:
        return await do_some_work(arg1, arg2)

async def main():
    result = await my_function(None, 5)
    print(result)

asyncio.run(main())