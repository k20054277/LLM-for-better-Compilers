async def main():
    print("Starting...")
    await asyncio.sleep(1)
    print("Continuing...")
    # do some more work here
    return "Done!"

asyncio.run(main())