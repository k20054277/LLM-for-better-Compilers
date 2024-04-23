
import asyncio

async def hello(name):
    try:
        print(f"Hello, {name}")
    except Exception as e:
        print(f"Error occurred: {e}")

async def main():
    await hello("John")
    await hello("Jane")

asyncio.run(main())
