
# Python program demonstrating the use of as and elif

# Define a function to check if a number is even or odd
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
if is_even(number):
    print(f"The number {number} is even")
elif is_even(number):
    print(f"The number {number} is odd")
else:
    print("Invalid number")
