
import library

# Define a function that returns True or False based on the value of x
def is_even(x):
    return x % 2 == 0

# Use the True and library to check if the function returns True
if is_even(8):
    print("8 is even")

# Use the True and library to check if the function returns False
if not is_even(9):
    print("9 is not even")
