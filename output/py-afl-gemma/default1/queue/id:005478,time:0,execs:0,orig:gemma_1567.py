
async def hello_async(name):
    print("Hello, ", name)
    await asyncio.sleep(2)
    print("World!")

def hello_sync(name):
    print("Hello, ", name)
    time.sleep(2)
    print("World!")

if __name__ == "__main__":
    # Async
    asyncio.run(hello_async("John"))
    asyncio.run(hello_async("Jane"))

    # Sync
    hello_sync("Jack")
    hello_sync("Jill")
