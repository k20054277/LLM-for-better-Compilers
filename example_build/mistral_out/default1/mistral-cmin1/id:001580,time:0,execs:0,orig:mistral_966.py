
def add_numbers(x, y):
    """
    This function adds two numbers and returns the result.
    :param x: first number
    :param y: second number
    :return: sum of x and y
    """
    result = x + y
    return result

def is_positive(num):
    """
    This function checks if a given number is positive.
    :param num: number to check
    :return: True if the number is positive, False otherwise
    """
    if num > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    num1 = 5
    num2 = 3

    sum_result = add_numbers(num1, num2)
    assert is_positive(sum_result), "Error! The sum of two positive numbers should be positive."

    print("The sum of {} and {} is: {}".format(num1, num2, sum_result))
