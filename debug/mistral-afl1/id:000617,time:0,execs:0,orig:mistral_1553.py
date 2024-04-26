
import asyncio

class FibGenerator:
    def __init__(self):
        self.a, self.b = 0, 1

    async def fib(self):
        while True:
            yield self.a
            self.a, self.b = self.b, self.a + self.b

@asyncio.coroutine
def main():
    generator = FibGenerator()
    fib_generator = asyncio.as_future(generator.fib())

    print("First 10 Fibonacci numbers:")
    for i in range(10):
        number = yield from fib_generator
        print(number)

if __name__ == "__main__":
    asyncio.run(main())
