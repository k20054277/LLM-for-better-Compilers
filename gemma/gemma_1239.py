
# This Python program demonstrates the use of AS and debugging

# Define a function called square
def square(x):
    return x ** 2

# Assign the square function to the variable y
y = square

# Print the value of y
print(y(5))

# Debugging:
# The above code has a bug in the square function. It squares the variable x instead of the parameter x. To fix the bug, we need to change the line square(x) to square(x) ** 2.

# Corrected code:
def square(x):
    return x ** 2

# Assign the square function to the variable y
y = square

# Print the value of y
print(y(5))

# Output:
# 25

# The above code demonstrates the use of AS and debugging. The AS keyword is used to assign the square function to the variable y, and the debugging process is used to identify and fix the bug in the code.
