import asyncio

async def main():
    data = ['apple', 'banana', 'cherry']
    print(f'Length of data: {len(data)}')
    await asyncio.sleep(1)
    print('After 1 second, the length is still: {len(data)}')

asyncio.run(main())