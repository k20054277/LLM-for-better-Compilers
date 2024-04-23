class AsyncClass:
    async def __init__(self):
        print("Initializing...")

    async def do_something(self):
        print("Doing something...")

async def main():
    obj = AsyncClass()
    await obj.do_something()
    print("Done.")

if __name__ == "__main__":
    asyncio.run(main())