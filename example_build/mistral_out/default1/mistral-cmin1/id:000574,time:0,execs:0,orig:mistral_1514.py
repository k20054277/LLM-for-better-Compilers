
# A simple program to demonstrate the use of assert and 'or' statement
def calc(num1, num2, operator):
    """
    This function performs basic arithmetic operations based on given operator.
    
    Args:
        num1 (int or float): First number
        num2 (int or float): Second number
        operator (str): Operator ('+', '-', '*', '/')

    Returns:
        result: Result of the operation
    """

    # Perform the arithmetic operation based on given operator
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        # Use 'or' to handle division by zero error
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error! Division by Zero is not allowed.")
            return None
    else:
        raise ValueError("Invalid Operator")

    # Use assert statement to validate the result
    assert result is not None, "Error! Result cannot be None."
    assert type(result) in [int, float], "Result should be either integer or float."
    
    return result

# Test cases for the function 'calc'
if __name__ == "__main__":

    # Test case 1: Addition
    print("Test Case 1: Addition")
    num1 = 5
    num2 = 3
    operator = "+"
    expected_result = 8
    actual_result = calc(num1, num2, operator)
    assert expected_result == actual_result, f"Expected {expected_result}, got {actual_result} instead."
    
    # Test case 2: Subtraction
    print("Test Case 2: Subtraction")
    num1 = 10
    num2 = 3
    operator = "-"
    expected_result = 7
    actual_result = calc(num1, num2, operator)
    assert expected_result == actual_result, f"Expected {expected_result}, got {actual_result} instead."
    
    # Test case 3: Multiplication
    print("Test Case 3: Multiplication")
    num1 = 5
    num2 = 3
    operator = "*"
    expected_result = 15
    actual_result = calc(num1, num2, operator)
    assert expected_result == actual_result, f"Expected {expected_result}, got {actual_result} instead."
    
    # Test case 4: Division
    print("Test Case 4: Division")
    num1 = 6
    num2 = 3
    operator = "/"
    expected_result = 2.0
    actual_result = calc(num1, num2, operator)
    assert expected_result == actual_result, f"Expected {expected_result}, got {actual_result} instead."
    
    # Test case 5: Division by zero
    print("Test Case 5: Division by Zero")
    num1 = 6
    num2 = 0
    operator = "/"
    calc(num1, num2, operator)  # Expecting an error here
