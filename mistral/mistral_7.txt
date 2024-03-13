
import asyncio

async def is_equal(x, y, delay=0):
    if x != y:
        print(f"'{x}' is not equal to '{y}'. Delaying result...")
        await asyncio.sleep(delay)
        print(f"Result: {x} is still not equal to {y}")
    else:
        print(f"'{x}' is equal to '{y}'")

async def main():
    x = 5
    y = 5
    await is_equal(x, y)

    x = 5
    y = 6
    await is_equal(x, y, 1.0)

if __name__ == "__main__":
    asyncio.run(main())
