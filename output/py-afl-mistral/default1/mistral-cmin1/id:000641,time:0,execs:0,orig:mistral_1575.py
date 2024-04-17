
import asyncio
import math

async def sqrt_calculator(number):
    result = math.sqrt(number)
    await asyncio.sleep(0.01)  # Simulate some computation time
    print(f"Square root of {number}: {result}")

async def main():
    tasks = [
        sqrt_calculator(2),
        sqrt_calculator(3),
        sqroot_calculator(4)
    ]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
