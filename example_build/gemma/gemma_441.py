
# This Python program demonstrates the use of False and compiler

# Define a function called is_even
def is_even(num):
    # Return True if num is even, False otherwise
    return num % 2 == 0

# Print the truth value of is_even(4)
print(is_even(4))  # Output: True

# Print the truth value of is_even(5)
print(is_even(5))  # Output: False

# Compile the function into a module
import compile

# Create a string containing the source code for the function
source_code = """
def is_even(num):
    return num % 2 == 0
"""

# Compile the source code into a module
compiled_module = compile.compile(source_code)

# Get the function object from the compiled module
compiled_function = compiled_module.getfunction("is_even")

# Print the truth value of compiled_function(4)
print(compiled_function(4))  # Output: True

# Print the truth value of compiled_function(5)
print(compiled_function(5))  # Output: False
