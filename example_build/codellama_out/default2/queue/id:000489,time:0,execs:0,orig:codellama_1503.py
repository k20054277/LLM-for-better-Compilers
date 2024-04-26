async def main():
    # create a coroutine object
    coro = my_coroutine()

    # schedule the coroutine to run asynchronously
    async_result = await asyncio.create_task(coro)

    # get the result of the coroutine
    result = async_result.result()

    # print the result
    print(result)

async def my_coroutine():
    # do some asynchronous work
    await asyncio.sleep(1)
    return "Hello, world!"

# run the main function asynchronously
asyncio.run(main())