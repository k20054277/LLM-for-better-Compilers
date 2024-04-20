# Example of using assert and batch in Python

def test_function(x, y):
    assert x > 0, "x must be positive"
    assert y < 10, "y must be less than 10"
    return x + y

if __name__ == '__main__':
    # Test the function with different values of x and y
    print(test_function(5, 2))  # Output: 7
    print(test_function(-5, 2))  # Output: AssertionError: x must be positive
    print(test_function(5, 12))  # Output: AssertionError: y must be less than