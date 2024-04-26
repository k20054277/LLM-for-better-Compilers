
import asyncio

class MyAsyncGenerator:
    def __aiter__(self):
        self.i = 0
        return self

    async def __anext__(self):
        if self.i < 5:
            self.i += 1
            await asyncio.sleep(1)
            return self.i
        else:
            raise StopAsyncIteration()

async def main():
    async with asyncio.get_event_loop() as loop:
        generator = MyAsyncGenerator()
        async for num in generator:
            print(f"Number: {num}")
            await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

# Here's an example of using repr()
def square_root(number):
    try:
        return number ** 0.5
    except ValueError:
        return f"Square root of {repr(number)} is not defined."

print(square_root(16))
print(square_root(-1))
