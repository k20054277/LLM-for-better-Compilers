
import asyncio

async def hello_world():
    print("Hello, world!")

async def main():
    await hello_world()

    print("Main event loop completed")

if __name__ == "__main__":
    asyncio.run(main())
