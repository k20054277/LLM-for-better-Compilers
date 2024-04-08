
# This Python program demonstrates the use of assert and +=

# Define a function to calculate the square of a number
def square(x):
    return x**2

# Assert that the square of 5 is 25
assert square(5) == 25

# Increment the value of x by 1
x += 1

# Assert that the square of x is 36
assert square(x) == 36

# Print the value of x
print(x)
