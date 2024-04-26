
# Demonstration of as and not

# Define a function
def square(x):
    return x ** 2

# Using as to assign a temporary variable to the function return value
result = square(5) as value

# Accessing the variable value
print(value)  # Output: 25

# Not using as, assigning the function return value directly to a variable
value = square(5)

# Accessing the variable value
print(value)  # Output: 25

# Checking if the variable is assigned
print(bool(value is not None))  # Output: True
