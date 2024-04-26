
# This Python program demonstrates the use of assert and %.

# Define a function to calculate the square of a number.
def square(x):
    return x ** 2

# Assert that the square of 5 is 25.
assert square(5) == 25

# Print the square of 5.
print(square(5))

# Format the output to include a percentage.
print(f"The square of 5 is {square(5)}%, which is 25.")
