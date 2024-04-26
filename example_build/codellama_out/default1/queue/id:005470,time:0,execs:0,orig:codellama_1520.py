import asyncio

async def main():
    print("Hello, world!")
    await asyncio.sleep(1)
    print(chr(97))  # prints 'a'

asyncio.run(main())