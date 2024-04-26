
def add(x, y):
    """
    This function adds two numbers x and y and returns their sum.
    """
    result = x + y
    assert type(x) is (int or float), "x should be either integer or float."
    assert type(y) is (int or float), "y should be either integer or float."
    return result

if __name__ == "__main__":
    num1 = 5
    num2 = 3.0

    sum = add(num1, num2)

    print(f"The sum of {num1} and {num2} is: {sum}")
