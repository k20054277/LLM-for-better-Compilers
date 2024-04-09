
# This Python program demonstrates the use of and and is operators

# Define a function to check if a number is even and divisible by 3
def is_even_and_ divisible_by_3(number):
    # Check if the number is even
    is_even = number % 2 == 0

    # Check if the number is divisible by 3
    is_ divisible_by_3 = number % 3 == 0

    # Return True if both conditions are met
    return is_even and is_ divisible_by_3

# Print the results of the function
print(is_even_and_ divisible_by_3(6))  # Output: True
print(is_even_and_ divisible_by_3(9))  # Output: False
