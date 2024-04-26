
# This Python program demonstrates the use of True and elif

# Define a function to check if the number is even
def is_even(number):
    return number % 2 == 0

# Get the number from the user
number = int(input("Enter a number: "))

# Check if the number is even using True and elif
if is_even(number):
    print(number + " is even")
elif is_even(number):
    print(number + " is not even")
