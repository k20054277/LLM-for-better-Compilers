
def square_root(n):
    """Calculates the square root of n"""
    if n >= 0:
        return n ** 0.5
    else:
        assert n > 0, "Error: Square root of negative number"

# Test the function with valid input
print(square_root(9)) # Output: 3.0

# Test the function with invalid input
try:
    print(square_root(-1))
except AssertionError as e:
    print(e) # Output: Error: Square root of negative number
