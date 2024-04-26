
import asyncio

# Callable coroutine for calculating the factorial of a given number
async def factorial(n):
    check = asyncio.get_event_loop().create_task(check_input(n))
    result = await check
    if result is None:
        raise ValueError("Factorial is not defined for negative numbers")
    return await calculate_factorial(n)

async def check_input(number):
    if number < 0:
        return None
    else:
        return number

async def calculate_factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
        await asyncio.sleep(0)
    return result

# Function to run the code
async def main():
    number = int(input("Enter a non-negative integer: "))
    try:
        result = await factorial(number)
        print(f"The factorial of {number} is {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())
