
import math

# Define a function that takes two arguments and returns their sum, with one argument set to None by default
def add_numbers(num1, num2=None):
    if num2 is None:
        print("Function called with only one argument. Adding None as the second argument.")
        num2 = 0

    # Perform addition using given numbers or adding None to a number
    result = num1 + num2

    print(f"The sum of {num1} and {num2} is {result}")

# Calling the function with one argument
add_numbers(5)

# Calling the function with two arguments
add_numbers(3, 4)

# Calling the function with one argument, None
add_numbers(7, None)
