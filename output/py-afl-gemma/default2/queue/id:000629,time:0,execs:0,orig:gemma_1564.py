
import asyncio

async def hello(name):
    print(f"Hello, {name}")
    await asyncio.sleep(1)
    print(f"Goodbye, {name}")

async def main():
    tasks = [hello(i) for i in ["Alice", "Bob", "Charlie"]]
    await asyncio.gather(*tasks)

asyncio.run(main())
