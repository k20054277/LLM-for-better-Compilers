# This program demonstrates the use of assert statement and data structures in Python

# Importing required modules
import math

# Defining a function to calculate the factorial of a number
def factorial(n):
    # Using assert statement to check if n is an integer
    assert type(n) == int, "n must be an integer"
    
    # Using for loop to calculate the factorial recursively
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

# Testing the function with different inputs
print("Testing the function with integer input:")
print(factorial(5)) # Output: 120
print("\nTesting the function with non-integer input:")
print(factorial(3.14)) # Output: AssertionError: n must be an integer

# Using a list as a data structure to store the factorials of different numbers
numbers = [1, 2, 3, 4, 5]
factors = []
for num in numbers:
    factors.append(factorial(num))
print("The factorials of the numbers are:", factors) # Output: The factorials of the numbers are: [1, 2, 6, 24, 120]