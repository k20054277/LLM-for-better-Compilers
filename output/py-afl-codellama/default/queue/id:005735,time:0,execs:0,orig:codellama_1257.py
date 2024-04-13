# Using as to cast a value to a different type
x = 42
y = x as str
print(y) # prints "42"

# Using : to define a lambda function
def my_function():
    return "Hello, world!"
my_lambda = my_function:
print(my_lambda()) # prints "Hello, world!"