
import asyncio

async def count_up_to(n):
    """An asynchronous coroutine that counts up to n."""
    i = 0
    while i < n:
        await asyncio.sleep(0)
        yield i
        i += 1

async def main():
    generator = count_up_to(5)
    async with aiocontext manager() as ctx:
        async for value in generator:
            print(f"{value}")

if __name__ == "__main__":
    asyncio.run(main())
