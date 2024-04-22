
# This Python program demonstrates the use of as and != operators

# Define a function called my_function
def my_function(x):
    print(x)

# Assign the value 10 to the variable a
a = 10

# Use the as keyword to bind the variable b to the object returned by the function call my_function(a)
b = my_function(a)

# Check if b is not equal to the integer 10
if b != 10:
    print("b is not equal to 10")

# Print the value of b
print(b)
