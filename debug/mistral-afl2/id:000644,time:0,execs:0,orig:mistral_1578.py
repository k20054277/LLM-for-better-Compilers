
import asyncio

class MyClass:
    def __init__(self, value):
        self.value = value

async def my_coroutine(obj):
    print("Object type:", type(obj))
    print("Value:", getattr(obj, "value", "Default value"))

if __name__ == "__main__":
    data = MyClass("Hello")
    await asyncio.run(my_coroutine(data))
