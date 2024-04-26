async def main():
    # some code here
    result = await some_async_function()
    # some more code here

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())