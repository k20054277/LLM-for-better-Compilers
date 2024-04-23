
import asyncio

# Function that returns a value after a delay (simulating I/O operation)
async def delayed_value(delay):
    await asyncio.sleep(delay)
    return 42

# Coroutine that demonstrates the usage of None and await
async def main():
    # Assigning None to a variable
    none_var = None

    print("None assignment:")
    print(f"none_var is {none_var}")

    # Using await with a coroutine that returns None
    await asyncio.sleep(1)
    none_coroutine = asyncio.create_task(asyncio.gather(*[delayed_value(i) for i in range(3)]))
    none_value = await none_coroutine
    print(f"none_value is {none_value}")

    # Using None as a default value for a coroutine function
    async def default_value(default=None):
        if default is not None:
            await asyncio.sleep(1)
            return default * 2

    default_coroutine = asyncio.create_task(default_value())
    default_value = await default_coroutine
    print(f"default_value is {default_value}")

if __name__ == "__main__":
    asyncio.run(main())
