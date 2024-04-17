
import asyncio

async def power(base, exponent):
    """Calculate base raised to the power of exponent asynchronously"""
    result = await asyncio.sleep(0.1)  # Simulate some computation
    return base ** exponent

@asyncio.coroutine
def main():
    """Main function using async/await syntax"""
    base = 2
    exponent = 8

    print("Calculating {} raised to the power of {}...".format(base, exponent))
    start = time()

    task = asyncio.ensure_future(power(base, exponent))
    result = yield from task

    end = time()
    duration = end - start
    print("Result: {}".format(result))
    print("Computation took: {:.3f} seconds".format(duration))

if __name__ == "__main__":
    asyncio.run(main())
