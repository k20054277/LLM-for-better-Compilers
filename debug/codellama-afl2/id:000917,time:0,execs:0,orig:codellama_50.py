async def main():
    print("Hello, world!")
    await asyncio.sleep(1)
    print("This is an async function.")

asyncio.run(main())