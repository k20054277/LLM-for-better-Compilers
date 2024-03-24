async def main():
    # do some work
    result = await long_running_task()
    if not result:
        print("The task failed")
    else:
        print("The task succeeded")

# define a function that returns a Future
def long_running_task():
    future = asyncio.get_event_loop().create_future()
    # simulate a long-running task
    time.sleep(5)
    if random.random() < 0.5:
        future.set_result(True)
    else:
        future.set_exception(Exception("The task failed"))
    return future

# run the main function
asyncio.run(main())