
# This Python program demonstrates the use of and and or operators

# Define a function to check if a number is even or odd
def is_even(num):
    return num % 2 == 0

# Define a function to check if a number is divisible by 3
def is_ divisible_by_3(num):
    return num % 3 == 0

# Check if a number is even or divisible by 3
num = 12

if is_even(num) or is_ divisible_by_3(num):
    print("Number is even or divisible by 3")
else:
    print("Number is not even or divisible by 3")
