
# Function to check if a list is empty or not
def check_empty_list(input_list):
    """
    This function checks if the given list is empty or not.
    :param input_list: The list to be checked
    :return: None
    """

    # Using assert statement to raise an error if the list is not empty
    assert len(input_list) == 0, "The list should be empty."

# Function to demonstrate check_empty_list function
def main():
    empty_list = []
    non_empty_list = [1, 2, 3]

    print("Checking empty list:")
    check_empty_list(empty_list)

    print("\nChecking non-empty list:")
    check_empty_list(non_empty_list)

if __name__ == "__main__":
    main()
