
import asyncio

async def add_numbers(x, y):
    result = x + y
    assert result is not None, f"Error: Result should not be None"
    return result

@asyncio.coroutine
def main():
    x = 5
    y = 3
    result = yield from add_numbers(x, y)

    # Here, we can safely use the result without worrying about errors
    print("Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
