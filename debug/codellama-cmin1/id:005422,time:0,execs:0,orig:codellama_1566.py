import asyncio

class MyClass:
    def __init__(self):
        self.value = 0

    async def increment(self):
        await asyncio.sleep(1)
        self.value += 1

async def main():
    obj = MyClass()
    print(obj.value)  # prints 0

    task = asyncio.create_task(obj.increment())
    await asyncio.gather(task)

    print(obj.value)  # prints 1

if __name__ == '__main__':
    asyncio.run(main())