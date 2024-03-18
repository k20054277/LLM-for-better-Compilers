
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        raise
    else:
        print(result)

# Example usage
divide(10, 2)  # Output: 5.0
divide(10, 0)  # Raises ZeroDivisionError
