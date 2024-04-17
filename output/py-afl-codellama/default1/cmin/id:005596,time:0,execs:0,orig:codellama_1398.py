# Define a constant
PI = 3.14

# Use the constant in an assertion
assert PI == 3.14, "The value of PI is not what we expected"

# Use the constant in a function
def calculate_area(radius):
    return PI * radius ** 2

# Test the function with different values for radius
print("Area of circle with radius 5:", calculate_area(5))
print("Area of circle with radius 10:", calculate_area(10))