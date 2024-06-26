
import asyncio

class FibGenerator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1

    async def fib_gen(self):
        while True:
            value = await asyncio.sleep(0.01)  # Sleep for a small duration to let other tasks run
            fib = self.a
            self.a, self.b = self.b, self.a + self.b
            yield from [fib] if fib <= self.limit else None

async def main():
    gen = FibGenerator(50)
    async with gen.fib_gen() as fib_generator:
        fibs = await asyncio.gather(*[next(fib_generator) for _ in range(10)])
        print(fibs)

if __name__ == "__main__":
    asyncio.run(main())
