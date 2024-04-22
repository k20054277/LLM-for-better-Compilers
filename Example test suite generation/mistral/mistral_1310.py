
# Example function with incorrect calculation
def square_root(n):
    return 0.5 * n

# Function under test
def calculate_square(number):
    sqrt = square_root(number)
    result = number * sqrt
    return result

if __name__ == "__main__":
    # Test cases
    num1 = 9
    num2 = -4
    num3 = 0

    # Test case with valid input
    print(f"Calculate square of {num1}: Expected: 8.485281, Actual:")
    actual = calculate_square(num1)
    assert abs(actual - 8.485281) < 0.01, f"Expected result to be close to 8.485281 but got {actual}"
    print(actual)

    # Test case with negative input
    print(f"\nCalculate square of {num2}: Expected: None (since the function doesn't support negative numbers), Actual:")
    try:
        actual = calculate_square(num2)
    except Exception as e:
        print(e)

    # Test case with zero input
    print(f"\nCalculate square of {num3}: Expected: 0, Actual:")
    actual = calculate_square(num3)
    assert actual == 0, f"Expected result to be 0 but got {actual}"
    print(actual)
