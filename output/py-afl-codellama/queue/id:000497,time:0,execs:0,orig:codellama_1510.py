# Demonstration of async and abs functions in Python

async def add(a, b):
    return a + b

async def subtract(a, b):
    return a - b

async def multiply(a, b):
    return a * b

async def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

async def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

# Example usage of the functions
a = await add(2, 3) # a == 5
b = await subtract(7, 3) # b == 4
c = await multiply(5, 6) # c == 30
d = await divide(10, 2) # d == 5
e = await absolute_value(-8) # e ==