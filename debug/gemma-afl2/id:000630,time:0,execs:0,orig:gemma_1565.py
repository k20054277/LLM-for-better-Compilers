
import asyncio

class AsyncClass:
    def __init__(self):
        self.data = None

    async def get_data(self):
        print("Waiting for data...")
        await asyncio.sleep(2)
        self.data = "Hello, world!"

    async def print_data(self):
        print("Data:", self.data)

async def main():
    async_class = AsyncClass()
    await async_class.get_data()
    await async_class.print_data()

asyncio.run(main())
