
# This Python program demonstrates the use of as and is

# Define a function called my_function
def my_function(x):
    print(x)

# Assign the value 10 to the variable a
a = 10

# Use as to assign the value of a to the variable b
b = a

# Use is to compare the identity of a and b
if a is b:
    print("a and b are the same object")

# Use as to assign a new object to the variable b
b = my_function(10)

# Use is to compare the identity of a and b
if a is not b:
    print("a and b are not the same object")

# Output
# 10
# a and b are the same object
# 10
# a and b are not the same object
