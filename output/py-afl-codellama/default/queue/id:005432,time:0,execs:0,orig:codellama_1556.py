import asyncio

async def main():
    with open('file.txt') as f:
        contents = await f.read()
    print(contents)

asyncio.run(main())