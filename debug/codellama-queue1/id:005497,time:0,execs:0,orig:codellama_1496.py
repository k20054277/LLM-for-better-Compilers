import asyncio

async def do_something():
    print("Doing something...")
    await asyncio.sleep(1)
    print("Finished doing something.")

async def main():
    if condition:
        await do_something()
    else:
        print("Condition not met.")

asyncio.run(main())