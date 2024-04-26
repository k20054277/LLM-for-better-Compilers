
import asyncio

async def print_numbers():
    for i in range(10):
        await asyncio.sleep(1)
        print(chr(i + 48))

async def main():
    await print_numbers()

if __name__ == "__main__":
    asyncio.run(main())
