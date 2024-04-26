
import asyncio

class MyClass:
    def __init__(self):
        self.data = None

    @asyncio.coroutine
    def get_data(self):
        # Simulate some asynchronous operation
        await asyncio.sleep(1)
        self.data = "Hello, world!"

    @asyncio.coroutine
    def get_data_classmethod(cls):
        # Simulate some asynchronous operation
        await asyncio.sleep(1)
        return "Hello, class!"

    def print_data(self):
        print(self.data)

    @classmethod
    def print_data_classmethod(cls):
        print(cls.get_data_classmethod())


async def main():
    my_class = MyClass()
    await my_class.get_data()
    my_class.print_data()

    await asyncio.gather(my_class.print_data_classmethod())


asyncio.run(main())
