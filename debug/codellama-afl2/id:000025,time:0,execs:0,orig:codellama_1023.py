import time

# as clause
print("Hello, world!")

# asynchronous function call
time.sleep(2)

# asyncio.gather()
async def main():
    await asyncio.gather(
        foo(),
        bar()
    )

async def foo():
    print("foo")

async def bar():
    print("bar")

if __name__ == '__main__':
    asyncio.run(main())