
import asyncio

async def task_a():
    print("Task A started.")
    await asyncio.sleep(1)
    print("Task A completed.")

async def task_b():
    try:
        print("Task B started.")
        await asyncio.sleep(0.5)
        raise Exception("Task B failed.")
    except Exception as e:
        print(f"Error in Task B: {e}")
        print("Handling exception in Task B...")
    finally:
        print("Task B completed with exception handling.")

async def task_c():
    print("Task C started.")
    await asyncio.sleep(2)
    print("Task C completed.")

async def main():
    print("Main function started.")
    await asyncio.gather(task_a(), task_b(), task_c())
    print("All tasks completed.")

if __name__ == "__main__":
    asyncio.run(main())
