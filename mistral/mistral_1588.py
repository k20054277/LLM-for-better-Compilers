
import asyncio

# Base class for asynchronous tasks
class AsyncTask:
    def __init__(self, func, *args, **kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs
        self._future = None

    @property
    def future(self):
        if not self._future:
            self._future = asyncio.Future()
            self._task = asyncio.ensure_future(self._run())
        return self._future

    async def _run(self):
        result = await self._func(*self._args, **self._kwargs)
        self._future.set_result(result)

class SlowAsyncTask(AsyncTask):
    def __init__(self, func, *args, **kwargs, delay=0.1):
        super().__init__(func, *args, **kwargs)
        self._delay = delay

    async def _run(self):
        print(f"Starting slow task: {self._func.__name__}")
        await asyncio.sleep(self._delay)
        result = await super()._run()
        print(f"Finished slow task: {self._func.__name__}")
        return result

@asyncio.coroutine
def main():
    slow_task = SlowAsyncTask(lambda: "Slow result", delay=1)
    fast_task = AsyncTask(lambda: "Fast result")

    tasks = [fast_task, slow_task]
    futures = [task.future for task in tasks]

    await asyncio.gather(*futures)

    results = [task.result() for task in tasks]
    print("Results:", results)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
