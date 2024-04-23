
import asyncio

# Nested function definition with nonlocal variable
def outer_function(initial_value):
    async def inner_function():
        # Use nonlocal keyword to access and modify the value of 'x' from the enclosing scope
        nonlocal x
        x += 1
        print(f"Inner function: current value of x is {x}")
        await asyncio.sleep(1)
        return x * 2
        
    x = initial_value
    result = await inner_function()
    print(f"Outer function: final value of x is {x} and result is {result}")
    return result

# Call the outer function with an initial value
async def main():
    result = await outer_function(5)
    print("The result of outer_function is:", result)

if __name__ == "__main__":
    asyncio.run(main())
