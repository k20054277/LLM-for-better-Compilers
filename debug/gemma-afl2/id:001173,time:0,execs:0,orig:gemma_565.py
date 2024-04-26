
# This Python program demonstrates the use of None and //=.

# Define a function that returns None
def no_return():
    return None

# Define a variable and assign None to it
a = None

# Use None in an if statement
if a is None:
    print("a is None")

# Use None as a default value for a variable
b = no_return()

# Use None to compare two variables
if b is None:
    print("b is None")

# Use None to assign a value to a variable
c = None

# Print the values of a, b, and c
print("a:", a)
print("b:", b)
print("c:", c)

# Use the //= operator to divide a number by 2 and assign the result to a variable
a //= 2

# Print the value of a
print("a:", a)
