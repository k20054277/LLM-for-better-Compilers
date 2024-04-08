
def add(x, y):
    """
    This function adds two numbers and returns the result.
    :param x: First number
    :param y: Second number
    :return: The sum of x and y
    """
    result = x + y
    assert type(x) is (int or float), "First parameter must be either integer or float"
    assert type(y) is (int or float), "Second parameter must be either integer or float"
    return result

def main():
    num1 = 5.0
    num2 = 3
    sum_of_numbers = add(num1, num2)

    print("The sum of {0} and {1} is {2}" .format(num1, num2, sum_of_numbers))

    # Testing the assert statement
    try:
        add("string1", 5)
    except AssertionError as e:
        print("Error message:", e)

    num3 = -5.0
    num4 = 2
    sum_of_numbers2 = add(num3, num4)

    if sum_of_numbers2 < (num3 + num4):
        print("Error: The sum of numbers is not correct")
    else:
        print("The sum of {0} and {1} is {2}" .format(num3, num4, sum_of_numbers2))

if __name__ == "__main__":
    main()
