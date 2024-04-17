
# A simple function to validate if a given number is positive
def validate_positive_number(n):
    """
    This function takes an integer as an argument and validates if it's positive.
    If the number is negative or zero, it raises an AssertionError with an error message.
    """
    assert n > 0, f"Error: The input number {n} must be positive."
    
# Now we can use this function to validate some numbers
try:
    # Valid input
    validate_positive_number(5)
except AssertionError as e:
    print(e)

# Invalid input
validate_positive_number(-3)
