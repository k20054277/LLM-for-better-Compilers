
# Define a namespace
my_namespace = {}

# Define a function within the namespace
def my_function(x):
    assert x >= 0
    return x * 2

# Access the function from the namespace
my_function(5)

# Assert fails if x is negative
my_function(-1)
