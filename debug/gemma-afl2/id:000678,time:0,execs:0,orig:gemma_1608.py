
import asyncio

async def hello(name):
    print(f"Hello, {name}")

async def main():
    names = ["John", "Jane", "Jack"]
    results = []
    for i, name in enumerate(names):
        await hello(name)
        results.append(i)

    print("Results:")
    print(results)

asyncio.run(main())
