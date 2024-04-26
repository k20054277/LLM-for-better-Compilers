
import asyncio

class DemoClass:
    async def __init__(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            self._data = await self._get_data()
        return self._data

    async def _get_data(self):
        # Simulate some asynchronous operation
        await asyncio.sleep(1)
        return "Hello, world!"

async def main():
    demo_obj = DemoClass()
    print(await demo_obj.data)

asyncio.run(main())
