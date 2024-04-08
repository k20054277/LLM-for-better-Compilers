
import asyncio
import threading

class Counter:
    def __init__(self, start=0):
        self._value = start

    async def increment(self):
        """Increment the counter's value."""
        self._value += 1
        print(f"Thread-{threading.current_thread().name}: Incremented the counter to {self._value}")

async def main():
    counter = Counter()

    # Create and run tasks that will increment the counter
    tasks = [asyncio.create_task(counter.increment()) for _ in range(5)]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    threading.stack_size(1024)  # Increase the stack size for threads to avoid a recursion error
    try:
        asyncio.run(main())
    finally:
        asyncio.get_event_loop().run_until_complete(asyncio.shutdown(asyncio.get_event_loop()))
