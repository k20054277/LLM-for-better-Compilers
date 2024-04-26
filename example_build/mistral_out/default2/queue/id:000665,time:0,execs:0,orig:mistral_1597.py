
import asyncio

async def fib():
    a, b = 0, 1
    while True:
        yield from asyncio.sleep(0)
        a, b = b, a + b

@asyncio.coroutine
async def main():
    generator = fib()
    fib_num = await next(generator)
    print("First Fibonacci number: ", fib_num)

    async for _ in asyncio.as_future(generator):
        fib_num = next(generator)
        print("Next Fibonacci number: ", fib_num)
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
