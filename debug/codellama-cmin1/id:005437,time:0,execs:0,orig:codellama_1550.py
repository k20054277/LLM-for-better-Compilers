import asyncio
from concurrent.futures import ThreadPoolExecutor

async def get_max(numbers):
    return max(numbers)

async def main():
    executor = ThreadPoolExecutor()
    future = asyncio.run_coroutine_threadsafe(get_max, executor, [1, 2, 3])
    result = await future
    print(result)

asyncio.run(main())