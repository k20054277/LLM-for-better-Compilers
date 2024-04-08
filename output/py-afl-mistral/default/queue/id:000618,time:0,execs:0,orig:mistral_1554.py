
import asyncio

async def greet(name):
    await asyncio.sleep(1)
    print(f"Hello, {name}!")

@asyncio.coroutine
def main():
    tasks = [greet("Alice"), greet("Bob")]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
