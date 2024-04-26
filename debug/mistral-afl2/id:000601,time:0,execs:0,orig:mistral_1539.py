
import asyncio

async def task_1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 completed")
    return "Result from Task 1"

async def task_2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")
    return "Result from Task 2"

async def main():
    task_1_result = await task_1()
    print(f"Task 1 result: {task_1_result}")

    if task_1_result == "Expected Result":
        print("If condition is met, proceeding to Task 2")
        task_2_result = await task_2()
        print(f"Task 2 result: {task_2_result}")
    else:
        print("If condition is not met, stopping the process")

if __name__ == "__main__":
    asyncio.run(main())
