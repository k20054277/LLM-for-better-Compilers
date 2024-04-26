
import asyncio
import time

async def print_numbers():
    number = 0
    while True:
        await asyncio.sleep(1)
        print(number)
        number += 1

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(print_numbers())
    loop.run_until_complete(task)
