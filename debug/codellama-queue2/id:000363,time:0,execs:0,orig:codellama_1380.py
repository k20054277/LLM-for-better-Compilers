import asyncio

async def wait(seconds):
    assert isinstance(seconds, int)
    await asyncio.sleep(seconds)
    return seconds

async def main():
    # Run the async function
    result = await wait(5)
    print(f"Waited {result} seconds")

if __name__ == "__main__":
    asyncio.run(main())