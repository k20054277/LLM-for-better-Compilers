
import asyncio
import threading

class Worker:
    def __init__(self, semaphore):
        self.semaphore = semaphore

    async def task(self):
        await self.semaphore.acquire()
        print(f"Worker {asyncio.current_task().coro_name} started.")
        await asyncio.sleep(1)
        print(f"Worker {asyncio.current_task().coro_name} finished.")
        self.semaphore.release()

async def main():
    semaphore = threading.Semaphore(3)  # Allow up to 3 concurrent tasks.
    workers = [Worker(semaphore) for _ in range(10)]
    await asyncio.gather(*[worker.task() for worker in workers])

if __name__ == "__main__":
    asyncio.run(main())
