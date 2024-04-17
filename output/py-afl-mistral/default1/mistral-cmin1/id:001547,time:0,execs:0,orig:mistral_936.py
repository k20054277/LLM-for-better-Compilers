
def is_perfect_square(n):
    """Return True if n is a perfect square."""

    # Base case: 1 is a perfect square
    if n == 1:
        return True

    # Check if the square root of n is an integer and recursively call the function
    if int(n ** 0.5) ** 2 == n:
        return True
    else:
        return False

# Test cases
print(is_perfect_square(4))   # True
print(is_perfect_square(16))  # True
print(is_perfect_square(27))  # False
