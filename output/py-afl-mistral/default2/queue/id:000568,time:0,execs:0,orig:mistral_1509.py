
def test_bitwise_operation(num1, num2):
    result = num1 & ~num2  # Bitwise AND operation with complement of num2

    assert result == num1, f"Expected {num1} but got {result}"

if __name__ == "__main__":
    test_bitwise_operation(5, 3)
    test_bitwise_operation(7, 5)
