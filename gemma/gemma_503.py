
# Demonstration of None and Namespace

# None is a special value in Python that represents the absence of any value.
print(None)  # Output: None

# Namespace is a global variable that stores functions and variables.
print(__namespace__)  # Output: <namespace '__main__'>

# Example of a function defined in the global namespace
def greet(name):
    print("Hello, " + name)

# Calling the function from the global namespace
greet("John")  # Output: Hello, John

# Variables defined in the global namespace
my_var = 10

# Accessing the variable from the global namespace
print(my_var)  # Output: 10

# Outputting the variables and functions defined in the global namespace
print(globals())  # Output: {'__doc__', '__name__', '__module__', 'greet', 'my_var'}
