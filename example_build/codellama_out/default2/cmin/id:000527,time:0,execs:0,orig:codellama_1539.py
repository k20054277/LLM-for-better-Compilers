import asyncio

async def my_function(arg1, arg2):
    """This is a docstring for the my_function function.
    
    It takes two arguments: arg1 and arg2.
    """
    await asyncio.sleep(3)  # simulate some work
    return arg1 + arg2

async def main():
    result = await my_function(1, 2)
    print(result)

if __name__ == '__main__':
    asyncio.run(main())