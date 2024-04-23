
import asyncio

async def divisible_by_three(n):
    """Checks if a number is divisible by 3 using async programming."""
    await asyncio.sleep(0.5)  # Simulate some delay
    return n % 3 == 0


async def main():
    # Create a list of numbers to check
    numbers = [i for i in range(1, 11)]

    # Use asyncio.gather to check if each number is divisible by 3
    results = await asyncio.gather([ divisible_by_three(n) for n in numbers ])

    # Print the results
    for i, result in enumerate(results):
        print(f"Number {numbers[i]} is divisible by 3? {result}")


if __name__ == "__main__":
    asyncio.run(main())
