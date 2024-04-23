
def is_even_and_positive(number):
    """
    Return True if number is both even and positive, False otherwise
    """
    return (number > 0) and (number % 2 == 0)

# Test the function with some examples
print(is_even_and_positive(5))   # False
print(is_even_and_positive(6))   # True
print(is_even_and_positive(-2))  # False
print(is_even_and_positive(0))   # True
