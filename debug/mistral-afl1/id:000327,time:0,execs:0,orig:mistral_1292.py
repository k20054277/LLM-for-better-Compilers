
def check_positive_numbers(numbers):
    """
    Function that checks if all the given numbers are positive and prints them out
    :param numbers: list of numbers
    :return: None
    """
    for number in numbers:
        assert number > 0, "Error: Number {} is not positive".format(number)
        print("Number: ", number)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    check_positive_numbers(numbers)
