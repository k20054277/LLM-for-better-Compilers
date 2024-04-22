async def main():
    try:
        await something_that_can_throw()
    except SomeException as e:
        print("Caught exception:", e)
    finally:
        print("Finally block ran")

async def something_that_can_throw():
    raise SomeException("Something went wrong")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())