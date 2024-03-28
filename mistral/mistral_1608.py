
import math
import asyncio

async def sqrt_and_round(number):
    """Calculate the square root of a number asynchronously and round it to 2 decimal places."""
    result = math.sqrt(number)
    rounded_result = round(result, 2)
    print(f'Square root of {number} is: {result} (exact)')
    print(f'Square root of {number} rounded to 2 decimal places is: {rounded_result}')

async def main():
    """Main function for asynchronous tasks."""
    await asyncio.gather(sqrt_and_round(25), sqrt_and_round(7.25))

if __name__ == "__main__":
    asyncio.run(main())
