
True and Namespace

# True is a boolean value that evaluates to True in boolean expressions
print(True)  # Output: True

# Namespace is a special object that stores variables and functions
my_namespace = Namespace()

# You can store variables in a namespace
my_namespace.my_variable = 10

# You can access variables from a namespace using the dot notation
print(my_namespace.my_variable)  # Output: 10

# You can also define functions in a namespace
def my_function(x):
    return x * 2

# You can access functions from a namespace using the dot notation
print(my_namespace.my_function(5))  # Output: 10

# True and namespace are two powerful tools in python programming
print(True and my_namespace)  # Output: True
