
def divide(numerator, denominator):
    """
    This function takes two arguments, numerator and denominator, and returns their quotient.
    Raises ZeroDivisionError if the denominator is zero.
    """

    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return numerator / denominator

try:
    result = divide(5, 2)
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error:", e.args[0])

# Let's check division by zero
result = divide(1, 0)
