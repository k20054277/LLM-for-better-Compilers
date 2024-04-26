
def calculate_sum(num1, num2):
    # Using assert statements to check input arguments
    assert type(num1) is int or type(num1) is float, "First argument must be either an integer or a floating-point number."
    assert type(num2) is int or type(num2) is float, "Second argument must be either an integer or a floating-point number."

    try:
        result = num1 / num2  # Simulating division by zero error
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")
        return None

    # Check if the first argument is greater than the second one
    if num1 <= num2:
        raise ValueError("First argument must be greater than the second one.")

    return num1 + num2

if __name__ == "__main__":
    num1 = 5.0
    num2 = 3.0
    sum_result = calculate_sum(num1, num2)

    if sum_result is not None:
        print(f"The sum of {num1} and {num2} is {sum_result}")
