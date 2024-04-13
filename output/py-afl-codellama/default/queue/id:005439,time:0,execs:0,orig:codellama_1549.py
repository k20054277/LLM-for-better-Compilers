import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed

async def compute(x):
    return x * 2

async def main():
    executor = ThreadPoolExecutor(max_workers=4)
    tasks = []
    for i in range(10):
        task = asyncio.ensure_future(compute(i))
        tasks.append(task)
    for i, future in enumerate(as_completed(tasks)):
        print(f"Result {i}: {await future}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())