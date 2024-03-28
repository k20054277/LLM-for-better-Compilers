
import asyncio

async def generate_numbers(start, stop):
    """Generator function that returns numbers asynchronously"""
    task = asyncio.create_task(self._generate_numbers_inner(start, stop))
    while True:
        number = await task
        if not number:
            break
        yield number

async def _generate_numbers_inner(self, start, stop):
    """Generator function for internal use"""
    current = start - 1
    while current >= stop:
        current -= 1
        yield current

async def print_numbers(numbers):
    """Prints numbers asynchronously"""
    task = asyncio.create_task(self._print_numbers_inner(numbers))
    await task

async def _print_numbers_inner(self, numbers):
    for number in numbers:
        print(number)
        await asyncio.sleep(0.1)

async def main():
    """Main function"""
    generator = await generate_numbers(5, 2)
    numbers = list(generator)
    await print_numbers(numbers[::-1])

if __name__ == "__main__":
    asyncio.run(main())
