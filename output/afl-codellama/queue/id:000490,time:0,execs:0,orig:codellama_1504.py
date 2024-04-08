import asyncio

async def main():
    try:
        await asyncio.sleep(1)
    except Exception as e:
        print("Exception occurred:", e)

asyncio.run(main())