import asyncio

async def main():
    dir_list = await dir('*')
    print(dir_list)

asyncio.run(main())