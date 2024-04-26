
# This Python program demonstrates the use of and and error handling

# Define a function to check if a number is even and divisible by 5
def is_even_and_ divisible_by_5(number):
    # Check if the number is even
    is_even = number % 2 == 0

    # Check if the number is divisible by 5
    is_ divisible_by_5 = number % 5 == 0

    # If both conditions are true, return True
    return is_even and is_ divisible_by_5

# Get the number from the user
number = int(input("Enter a number: "))

# Check if the number is even and divisible by 5
if is_even_and_ divisible_by_5(number):
    print(f"The number {number} is even and divisible by 5")
else:
    # Raise an error
    raise ValueError("The number is not even and divisible by 5")

# Handle the error
try:
    print(is_even_and_ divisible_by_5(number))
except ValueError as e:
    print(e)
