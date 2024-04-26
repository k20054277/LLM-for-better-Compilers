
# This Python program demonstrates the use of assert and print

# Define a function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Assert that the function returns True for even numbers
assert is_even(4) is True

# Assert that the function returns False for odd numbers
assert is_even(5) is False

# Print the result of the assert statements
print("All assert statements are successful!")

# Print the value of the variable num
print("The value of num is:", num)
