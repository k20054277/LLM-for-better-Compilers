
# Define a function with expected preconditions
def divide(x, y):
    assert y != 0, "Error: Division by zero is not allowed"
    return x / y

# Test cases for divide function
if __name__ == "__main__":
    # Test case 1: Divide by a non-zero number
    result = divide(10, 2)
    assert result > 3.5, "Error: Expected result to be greater than 3.5"
    print("Test case 1 passed")

    # Test case 2: Divide by zero
    try:
        result = divide(10, 0)
    except AssertionError as e:
        print(e)
    else:
        assert False, "Expected an AssertionError but did not get one"
    finally:
        print("Test case 2 failed")

# Test case 3: Divide by a positive number
result = divide(10, 4)
assert result > 2, "Error: Expected result to be greater than 2"
print("Test case 3 passed")
