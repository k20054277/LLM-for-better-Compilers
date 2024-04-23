
def calculate_sum(num1, num2):
    # Using assert to check if the input arguments are numbers
    assert isinstance(num1, (int, float)), "First argument must be a number"
    assert isinstance(num2, (int, float)), "Second argument must be a number"

    # Using or operator to check if either of the condition is true
    if num1 > 0 and num2 > 0:
        print("Both numbers are positive")
        return num1 + num2
    elif num1 < 0 and num2 < 0:
        print("Both numbers are negative")
        return num1 + num2
    else:
        print("One or both numbers are zero")
        return 0

if __name__ == "__main__":
    # Testing the function with valid input
    x = 5
    y = 7
    result = calculate_sum(x, y)
    print(f"The sum of {x} and {y} is: {result}")

    # Testing the function with invalid input (non-numbers)
    try:
        calculate_sum("a", "b")
    except AssertionError as error:
        print(error)
