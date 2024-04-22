
# This Python program demonstrates the use of None and *=

# Define a function
def multiply(x, y):
    # Return None if x is None
    if x is None:
        return None

    # Multiply x and y
    return x * y

# Get two numbers
a = 10
b = None

# Multiply the two numbers
product = multiply(a, b)

# Print the product
if product is not None:
    print(product)
else:
    print("No product")
