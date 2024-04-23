import asyncio

async def coro1():
    print("Coroutine 1")
    await asyncio.sleep(1)

async def coro2():
    print("Coroutine 2")
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(coro1(), coro2())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())