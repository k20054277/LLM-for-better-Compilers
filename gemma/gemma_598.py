
# This Python program demonstrates the use of True and else

# Define a function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is even using True and else
if is_even(number):
    print(f"The number {number} is even")
else:
    print(f"The number {number} is not even")
