
# A function for addition operation
def add(num1, num2, is_sum=True):
    """
    This function takes two numbers as arguments and performs their addition based on given boolean flag 'is_sum'
    :param num1: first number
    :param num2: second number
    :param is_sum: a boolean value to indicate if we want to perform the sum or not (default: True)
    :return: the result of addition
    """
    if is_sum:
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
    else:
        print("Performing an operation other than sum")

# Testing the function with different scenarios
add(5, 3)                       # Performs addition
add(7, 8, False)                # Does not perform addition and prints a message instead
