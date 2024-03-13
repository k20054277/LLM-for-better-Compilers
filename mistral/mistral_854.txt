
# This example checks if a number is positive and even
def is_positive_even(number):
    """
    This function checks if a given number is positive and even.
    :param number: An integer number.
    :return: True if the number is positive and even, False otherwise.
    """
    return number > 0 and number % 2 == 0

if __name__ == "__main__":
    num = int(input("Enter an integer: "))

    if is_positive_even(num):
        print(f"{num} is a positive even number.")
    else:
        if num > 0:
            print(f"{num} is a positive odd number or a negative number.")
        else:
            print(f"{num} is a negative even number.")
