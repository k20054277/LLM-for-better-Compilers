
# This Python program demonstrates the use of assert and bin functions

# Define a function to demonstrate assert and bin
def my_function(num):
    assert num % 2 == 0
    return bin(num)

# Test the function with different numbers
my_function(4)  # Output: 'bin(4) = 100'
my_function(6)  # Output: 'bin(6) = 110'
my_function(7)  # Output: 'AssertionError: number must be even'

# Print the return value of the function
print(my_function(4))
