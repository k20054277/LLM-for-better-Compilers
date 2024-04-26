
# This Python program demonstrates the use of and and or operators

# Define a function to check if a number is even or odd
def is_even(num):
    return num % 2 == 0

# Define a function to check if a number is divisible by 3
def is_ divisible_by_3(num):
    return num % 3 == 0

# Use the and operator to check if a number is even and divisible by 3
def is_even_and_ divisible_by_3(num):
    return is_even(num) and is_ divisible_by_3(num)

# Use the or operator to check if a number is even or divisible by 3
def is_even_or_ divisible_by_3(num):
    return is_even(num) or is_ divisible_by_3(num)

# Print the results of the functions
print(is_even(4))  # Output: True
print(is_even_and_ divisible_by_3(6))  # Output: True
print(is_even_or_ divisible_by_3(5))  # Output: True
print(is_even_and_ divisible_by_3(9))  # Output: False
print(is_even_or_ divisible_by_3(11))  # Output: False
