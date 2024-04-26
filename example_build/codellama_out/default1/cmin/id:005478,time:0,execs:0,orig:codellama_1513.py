import asyncio
from typing import Any

async def my_coroutine(arg: Any) -> None:
    print("Starting coroutine...")
    # Do some work here...
    await asyncio.sleep(1)  # Simulate some work being done
    print("Coroutine finished!")

async def main() -> None:
    my_arg = "Hello, world!"
    task = asyncio.create_task(my_coroutine(my_arg))
    await task

asyncio.run(main())