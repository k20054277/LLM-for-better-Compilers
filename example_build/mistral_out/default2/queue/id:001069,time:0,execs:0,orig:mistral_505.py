
import asyncio

# A simple function that returns a Promise (future) that resolves after given delay.
async def sleep(seconds):
    await asyncio.sleep(seconds)
    return "Slept for {} seconds.".format(int(seconds))

# An asynchronous coroutine function that prints "Hello, World!" and then waits for 3 seconds.
async def main():
    print("Hello, World!")
    await sleep(3)
    print("Done.")

# Run the coroutine using asyncio's `run()` function.
if __name__ == "__main__":
    try:
        # The event loop will run the coroutine and wait for it to complete.
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting gracefully...")
