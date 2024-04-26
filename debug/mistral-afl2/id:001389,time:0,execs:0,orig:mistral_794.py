
import asyncio

async def task_1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 completed")
    return "Result from task 1"

async def task_2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")
    return "Result from task 2"

async def main():
    result_task_1 = await task_1()
    result_task_2 = await task_2()

    if result_task_1 == "Expected result from task 1" and result_task_2 == "Expected result from task 2":
        print("Both tasks completed successfully")
    else:
        print("An error occurred, as one or both of the tasks did not complete successfully")

if __name__ == "__main__":
    asyncio.run(main())
