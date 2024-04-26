
# This Python program demonstrates the use of the and and oct operators.

# Define a variable with an integer value.
x = 10

# Use the and operator to check if x is greater than 5 and less than 15.
if x > 5 and x < 15:
    print("x is greater than 5 and less than 15.")

# Use the oct operator to convert x to an octal string.
oct_str = str(x, oct)

# Print the octal string.
print("The octal string representation of x is:", oct_str)
