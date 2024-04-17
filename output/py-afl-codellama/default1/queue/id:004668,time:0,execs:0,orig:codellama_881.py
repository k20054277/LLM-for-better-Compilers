# Using "and" with "pow" to find if a number is a perfect square or not
def is_perfect_square(n):
    return n > 0 and pow(n, 0.5) % 1 == 0

# Testing the function
print(is_perfect_square(4))   # True
print(is_perfect_square(-4))  # False
print(is_perfect_square(8))   # True