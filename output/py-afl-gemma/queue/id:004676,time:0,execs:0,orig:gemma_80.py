
# This Python program demonstrates the use of and and if

# Define a function to check if a number is even and divisible by 5
def is_even_and_ divisible_by_5(num):
    # Check if the number is even
    is_even = num % 2 == 0

    # Check if the number is divisible by 5
    is_ divisible_by_5 = num % 5 == 0

    # If the number is even and divisible by 5, return True
    return is_even and is_ divisible_by_5

# Check if 10 is even and divisible by 5
if is_even_and_ divisible_by_5(10):
    print("10 is even and divisible by 5")

# Check if 15 is even and divisible by 5
if is_even_and_ divisible_by_5(15):
    print("15 is even and divisible by 5")
