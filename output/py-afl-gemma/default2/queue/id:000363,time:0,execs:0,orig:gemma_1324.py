
# This Python program demonstrates the use of assert and del

# Define a function to test
def square(x):
    return x ** 2

# Assert that square(5) is equal to 25
assert square(5) == 25

# Delete the variable x
del x

# Try to use the variable x, but it should raise a NameError
try:
    print(x)
except NameError:
    print("x is not defined")

# Print the output
print("The program has completed.")
