
# This Python program demonstrates the use of assert and algorithm

# Define a function to find the maximum of two numbers
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

# Assert that the function returns the correct maximum
assert find_max(5, 10) == 10
assert find_max(10, 5) == 10

# Algorithm to find the maximum of two numbers using recursion
def find_max_recursive(a, b):
    if a > b:
        return a
    else:
        return b

# Assert that the recursive function returns the correct maximum
assert find_max_recursive(5, 10) == 10
assert find_max_recursive(10, 5) == 10

# Print the maximum
print("The maximum is:", find_max(5, 10))
print("The maximum is:", find_max_recursive(5, 10))
