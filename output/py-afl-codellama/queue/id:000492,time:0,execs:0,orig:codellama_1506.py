import asyncio

async def do_something():
    try:
        await some_async_function()
    except Exception as e:
        print(f"Error occurred: {e}")

async def main():
    try:
        await do_something()
    except Exception as e:
        print(f"Main function error: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())