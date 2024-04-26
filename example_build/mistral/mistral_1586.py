
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    print("Main function started")
    await asyncio.gather(task1(), task2())
    print("Main function completed")

if __name__ == "__main__":
    asyncio.run(main())
