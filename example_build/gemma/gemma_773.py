
# Import the True module
import true

# Define a function that returns True or False
def is_even(num):
    return num % 2 == 0

# Use True to check if the function returns True
if is_even(8) is True:
    print("8 is even")

# Use True to check if the function returns False
if is_even(9) is False:
    print("9 is not even")

# Use True to compare two booleans
if True == False:
    print("True is not equal to False")

# Use True to negate a boolean
if not True:
    print("True is negated to False")
