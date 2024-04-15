import asyncio

async def main():
    # Use "await" to wait for one of two tasks to complete
    result = await asyncio.gather(task1(), task2())
    print(result)

# Define two tasks that return a value
async def task1():
    return 42

async def task2():
    return 99

if __name__ == '__main__':
    asyncio.run(main())