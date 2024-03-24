
# This Python program demonstrates the use of True and exception

# Define a function to check if a number is even
def is_even(num):
    # If the number is even, return True
    if num % 2 == 0:
        return True
    # Otherwise, raise an exception
    else:
        raise ValueError("The number is not even")

# Try to check if 6 is even
try:
    if is_even(6):
        print("6 is even")
except ValueError as e:
    # Catch the exception and print the error message
    print("Error:", e)

# Try to check if 5 is even
try:
    if is_even(5):
        print("5 is even")
except ValueError as e:
    # Catch the exception and print the error message
    print("Error:", e)
