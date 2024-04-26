
# This Python program demonstrates the use of as and while.

# Define a function to print squares of numbers.
def square(n):
    return n ** 2

# Create a list of numbers.
numbers = [1, 2, 3, 4, 5]

# Use as and while to print squares of numbers.
for num in numbers:
    as square_value := square(num)
    while square_value < 10:
        print(square_value)
