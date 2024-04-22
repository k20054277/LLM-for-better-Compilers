
import asyncio

class MyClass:
    def __init__(self, value):
        self.value = value

@asyncio.coroutine
def print_and_check(obj):
    print("Object is:", obj)
    if isinstance(obj, MyClass):
        print(f"Instance of MyClass: Yes")
    else:
        print(f"Instance of MyClass: No")

@asyncio.coroutine
def main():
    obj1 = MyClass(42)
    task1 = asyncio.create_task(print_and_check(obj1))

    obj2 = 42
    task2 = asyncio.create_task(print_and_check(obj2))

    await asyncio.gather(*[task for task in (task1, task2)])

if __name__ == "__main__":
    asyncio.run(main())
