
import numpy as np

# Function with None as default value
def divide(a, b=None):
    """
    Divide two numbers a and b. If b is not provided, the function returns None.
    :param a: A number for dividend.
    :param b: A number for divisor (default: None).
    :return: Result of division or None if b is not provided.
    """
    if b is not None:
        result = np.divide(a, b)
        return result
    else:
        print("Function received no divisor. Returning None.")
        return None

# Test the divide function with some inputs
print(divide(5))
print(divide(10, 3))
print(divide(4, None))
