
import asyncio

# Define a frozenset of tasks
tasks = frozenset([1, 2, 3])

async def task(number):
    print(f"Task {number} started")
    await asyncio.sleep(1)
    print(f"Task {number} completed")

@asyncio.coroutine
async def main():
    tasks_list = [task(num) for num in tasks]
    await asyncio.wait(tasks_list)

if __name__ == "__main__":
    asyncio.run(main())
