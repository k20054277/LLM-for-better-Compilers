
# This Python program demonstrates the use of and and type

# Define a function to check if a number is even and divisible by 5
def is_even_and_ divisible_by_5(number):
    # Check if the number is even
    is_even = number % 2 == 0

    # Check if the number is divisible by 5
    is_ divisible_by_5 = number % 5 == 0

    # Return True if both conditions are met
    return is_even and is_ divisible_by_5

# Print the result of the function
print(is_even_and_ divisible_by_5(10))  # Output: True
print(is_even_and_ divisible_by_5(25))  # Output: False
