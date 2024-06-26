import asyncio
from enum import Enum

class TaskStatus(Enum):
    RUNNING = "running"
    COMPLETED = "completed"

async def fetch_data(url: str) -> str:
    # Fetch data from the URL and return it as a string
    return "Some data"

async def main():
    tasks = [fetch_data("http://example.com"), fetch_data("http://example2.com")]
    for task in enumerate(tasks):
        print(task)
        if task[1] == TaskStatus.COMPLETED:
            print(f"Task {task[0]} completed with data: {task[1]}")

asyncio.run(main())