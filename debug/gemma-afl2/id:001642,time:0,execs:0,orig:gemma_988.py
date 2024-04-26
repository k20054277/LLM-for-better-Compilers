
# Demonstrate the use of and and namespace

# Define a namespace
my_namespace = __dict__

# Define a function within the namespace
def my_function():
    print("Hello, world!")

# Access the function from the namespace
my_namespace["my_function"]()

# Use the and operator to combine two boolean expressions
if 5 > 2 and 3 < 6:
    print("The condition is true")

# Print the value of the namespace
print(my_namespace)
