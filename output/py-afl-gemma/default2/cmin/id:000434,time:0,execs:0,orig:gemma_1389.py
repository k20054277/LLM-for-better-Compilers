
# This Python program demonstrates the use of assert and min

# Define a function to find the minimum of two numbers
def find_minimum(num1, num2):
    return min(num1, num2)

# Assert that the function returns the minimum of the two numbers
assert find_minimum(5, 10) == 5

# Print the minimum value
print("The minimum value is:", find_minimum(5, 10))
