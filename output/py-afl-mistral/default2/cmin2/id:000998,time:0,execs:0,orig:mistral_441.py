
# Example demonstrating the use of None

def is_none(value):
    """
    Check if given value is equal to None
    :param value: Any Python object
    :return: Boolean value
    """
    return value is None

def main():
    # Assigning None to a variable
    my_variable = None

    print("my_variable is None? ", is_none(my_variable))

    # Assigning other values
    another_variable = 42
    third_variable = "Hello, World!"

    print("another_variable is None? ", is_none(another_variable))
    print("third_variable is None? ", is_none(third_variable))

if __name__ == "__main__":
    main()
