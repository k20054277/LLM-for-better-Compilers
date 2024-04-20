import asyncio

async def greet(name):
    return f"Hello, {name}!"

def main():
    name = "Alice"
    result = await greet(name)
    print(result)

asyncio.run(main())