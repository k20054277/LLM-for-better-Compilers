
# Define a namespace
my_namespace = {}

# Assign variables to the namespace
my_namespace.my_variable = 10
my_namespace.my_function = lambda x: x * 2

# Accessing variables and functions from the namespace
print(my_namespace.my_variable)  # Output: 10
print(my_namespace.my_function(5))  # Output: 10

# Using as to bind a namespace to a variable
my_alias = my_namespace

# Accessing variables and functions from the alias
print(my_alias.my_variable)  # Output: 10
print(my_alias.my_function(5))  # Output: 10

# Output: 10
print(my_namespace.my_variable)

# Output: 10
print(my_alias.my_variable)
