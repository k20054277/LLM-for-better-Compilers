
# Function that calculates the square root using lambda function
square_root = lambda x: x ** 0.5 if x >= 0 else AssertionError("Square root can't be calculated for negative numbers")

# Function that checks if a number is even using lambda function and assert statement
is_even = lambda x: assert x % 2 == 0, f"{x} is not an even number"

# Testing the functions
print(square_root(9))
print(square_root(4))
print(square_root(3))

print("----")

print(is_even(10))
print(is_even(5))
