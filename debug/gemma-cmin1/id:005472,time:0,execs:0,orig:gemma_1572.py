
async def foo(x):
    try:
        print("Before await")
        await asyncio.sleep(2)
        print("After await")
    finally:
        print("Finally")

asyncio.run(foo(1))
