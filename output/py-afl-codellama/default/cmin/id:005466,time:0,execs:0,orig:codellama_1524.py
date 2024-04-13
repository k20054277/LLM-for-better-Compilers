import asyncio

class MyObject:
    def __init__(self):
        self.x = 5

    async def my_method(self):
        delattr(self, "x")
        print("X has been deleted!")

async def main():
    obj = MyObject()
    await obj.my_method()

asyncio.run(main())