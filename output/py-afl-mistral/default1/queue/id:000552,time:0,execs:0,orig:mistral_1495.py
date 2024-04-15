
def validate_input(user_input):
    """
    This function validates user input and uses assert to check if it's an integer.
    """
    try:
        num = int(user_input)
    except ValueError:
        print("Error: Input must be an integer.")
        assert type(user_input) is int, "Input must be an integer."
    return num

def add_numbers(num1, num2):
    """
    This function adds two numbers and checks if the result is as expected using ==.
    """
    sum = num1 + num2
    assert sum == (num1 + num2), f"Error: The sum of {num1} and {num2} is not correct."
    return sum

if __name__ == "__main__":
    user_input1 = input("Enter the first number: ")
    user_input2 = input("Enter the second number: ")

    num1 = validate_input(user_input1)
    num2 = validate_input(user_input2)

    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")
