
# This Python program demonstrates the use of and and elif statements.

# Define a function to check if a number is even and divisible by 3.
def is_even_and_ divisible_by_3(num):
    # Check if the number is even.
    is_even = num % 2 == 0

    # Check if the number is divisible by 3.
    is_ divisible_by_3 = num % 3 == 0

    # If the number is even and divisible by 3, return True.
    return is_even and is_ divisible_by_3

# Check if 12 is even and divisible by 3.
if is_even_and_ divisible_by_3(12):
    print("12 is even and divisible by 3.")

# Check if 15 is even and divisible by 3.
elif is_even_and_ divisible_by_3(15):
    print("15 is not even but divisible by 3.")

# Otherwise, print an error message.
else:
    print("Error: The number is not even or divisible by 3.")
