
import asyncio

class AsyncObject:
    def __init__(self, name):
        self.name = name

    async def say_hello(self):
        print("Hello, ", self.name)

async def main():
    # Create an asynchronous object
    async_object = AsyncObject("John")

    # Call the async method on the object
    await async_object.say_hello()

    print("Program finished")

asyncio.run(main())
