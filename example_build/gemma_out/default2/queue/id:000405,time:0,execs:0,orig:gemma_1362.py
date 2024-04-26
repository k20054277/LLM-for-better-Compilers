
# This Python program demonstrates the use of assert and dir functions

# Define a function called my_function
def my_function(x):
    return x * 2

# Assert that the value returned by my_function(5) is 10
assert my_function(5) == 10

# Print the attributes and methods of the my_function object
print(dir(my_function))

# Output:
# ['__doc__', '__dict__', '__module__', '__name__', '__weakref__', '__call__', '__class__', 'my_function']
