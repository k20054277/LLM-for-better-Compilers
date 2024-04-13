
import asyncio

async def nonlocal_async(n):
    nonlocal x
    x = n
    print(x)

async def main():
    await asyncio.gather(*[nonlocal_async(i) for i in range(5)])

asyncio.run(main())
