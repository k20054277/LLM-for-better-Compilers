
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        raise CustomException("Cannot divide by zero")
    return result

def test_divide():
    assert 5 >= 3, "Five is not greater than or equal to three"
    x = 10
    y = 2
    expected_result = 5.0
    result = divide(x, y)
    assert result == expected_result, f"Divide {x} by {y} did not return expected value {expected_result}"

if __name__ == '__main__':
    try:
        test_divide()
    except CustomException as e:
        print(f"Error: {e}")
