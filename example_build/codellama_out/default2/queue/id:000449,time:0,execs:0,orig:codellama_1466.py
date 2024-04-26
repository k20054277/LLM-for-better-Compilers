# Import the math module
math = __import__('math')

# Check if the math module is defined
assert math, "The math module is not defined"

# Use the math module
print(math.pi)