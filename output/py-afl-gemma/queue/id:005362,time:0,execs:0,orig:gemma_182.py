
# This Python program demonstrates the use of and and bool

# Define a function to check if a number is even and divisible by 3
def is_even_and_ divisible_by_3(num):
    # Check if the number is even
    is_even = num % 2 == 0

    # Check if the number is divisible by 3
    is_ divisible_by_3 = num % 3 == 0

    # Return True if both conditions are met, False otherwise
    return is_even and is_ divisible_by_3

# Check if 12 is even and divisible by 3
is_even_and_ divisible_by_3(12)

# Output: True
print(is_even_and_ divisible_by_3(12))

# Check if 15 is even and divisible by 3
is_even_and_ divisible_by_3(15)

# Output: False
print(is_even_and_ divisible_by_3(15))
