
def is_positive_and_even(num):
    """
    This function checks if a number is both positive and even
    :param num: an integer
    :return: True if the number is positive and even, False otherwise
    """
    return num > 0 and num % 2 == 0

# Test some numbers
for num in [4, 3, -5, 10]:
    print(f'{num} is {"" if is_positive_and_even(num) else "not"} positive and even')
