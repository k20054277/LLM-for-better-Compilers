# Example 1: Using assert to check for a specific condition

def my_function(x):
    assert x > 0, "The value of x must be positive"
    return x**2

my_function(-5)  # This will raise an AssertionError because the value of x is negative