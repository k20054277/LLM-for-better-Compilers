
async def my_async_function(x):
    print(x)
    await asyncio.sleep(1)
    print(x + 1)

async def main():
    my_async_function(5)
    print("Main is continuing")

    # Del keyword is used to remove the reference of the function object
    del my_async_function

    print("Main has completed")

asyncio.run(main())
