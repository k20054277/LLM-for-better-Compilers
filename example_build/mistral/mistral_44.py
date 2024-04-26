
# Define some functions
def func1():
    print("Function 1 called")

def func2():
    print("Function 2 called")

# False is a built-in constant representing false value. It's equivalent to the boolean value 0.
false_value = False

# callable() is a built-in function that returns True if an object is callable or False otherwise.
def is_callable(obj):
    return callable(obj)

# Demonstrate the use of False
if false_value:
    print("False is not true")
else:
    print("False is indeed false")

# Demonstrate the use of callable()
functions = [func1, func2]
for func in functions:
    if is_callable(func):
        func()
