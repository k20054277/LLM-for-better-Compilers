# This program demonstrates the use of False and compiler

# Define a function that takes a boolean argument and returns its negation
def negate(x):
    return not x

# Test the function with different values for x
print(negate(True))  # Output: False
print(negate(False))  # Output: True

# Use the compiler to compile a string of Python code and execute it
import compile

code = "print('Hello, world!')"
compile.execute(code)  # Output: Hello, world!