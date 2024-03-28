
# This Python program demonstrates the use of True and arguments

def my_function(x, y, z=True):
    print(x)
    print(y)
    print(z)

# Calling the function with different arguments and True as the default for z
my_function(10, 20, True)

# Calling the function with different arguments and False as the value for z
my_function(10, 20, False)
