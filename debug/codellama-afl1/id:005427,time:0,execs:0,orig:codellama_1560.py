async def main():
    for i in range(5):
        print(f"Processing {i}")
        await asyncio.sleep(1)

asyncio.run(main())