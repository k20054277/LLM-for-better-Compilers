import asyncio

class MyClass:
    def __init__(self):
        self.x = 5

    async def my_method(self):
        print(f"Inside method: x = {self.x}")
        await asyncio.sleep(1)
        print(f"After sleeping: x = {self.x}")

my_object = MyClass()

# Use getattr to access the my_method attribute of my_object
# and pass it to the async function
async def run():
    await asyncio.gather(getattr(my_object, "my_method")())

asyncio.run(run())