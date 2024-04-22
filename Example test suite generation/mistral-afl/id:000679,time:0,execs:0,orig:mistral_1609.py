
import asyncio

class Task:
    def __init__(self, name, function):
        self.name = name
        self.function = function
        self.future = asyncio.Future()

    async def run(self):
        print(f"Starting task {self.name}")
        try:
            result = await self.function()
            self.future.set_result(result)
        except Exception as e:
            self.future.set_exception(e)
        finally:
            print(f"Finished task {self.name}")

async def main():
    tasks = set()

    async for i in range(5):
        task = Task(f"Task_{i}", lambda: asyncio.sleep(1))
        tasks.add(task)
        await task.run()

    print("All tasks completed")

async def handle_completed_tasks():
    while tasks:
        task = tasks.pop()
        result = task.future.result()
        print(f"Task {task.name} completed with result: {result}")

async def main_entry_point():
    tasks = set()

    loop = asyncio.get_event_loop()

    await loop.create_task(main())
    await loop.create_task(handle_completed_tasks())

    loop.run_until_complete()

if __name__ == "__main__":
    main_entry_point()
