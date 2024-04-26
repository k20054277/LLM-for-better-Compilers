
def is_even(num):
    """
    This function checks if a number is even or not.
    :param num: An integer number
    :return: bool - returns True if the number is even, False otherwise
    """
    return num % 2 == 0

def main():
    print("Is 5 even? " + str(is_even(5)))

if __name__ == "__main__":
    main()
