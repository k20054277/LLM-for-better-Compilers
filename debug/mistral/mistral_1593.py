
import asyncio
from aioiter import map as aiomap

async def func(x):
    await asyncio.sleep(0.1)  # Replace with your async function logic
    return x * x

async def main():
    data = list(range(5))
    async for result in aiomap(func, data):
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
