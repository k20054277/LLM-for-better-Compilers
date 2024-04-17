
def calculate_root(number):
    """
    Calculate the square root of given number.
    :param number: Number to find the square root of.
    :return: The calculated square root.
    """

    # Using assert statement to check if number is positive
    assert number >= 0, "Error! Number should be non-negative."

    try:
        result = float(number) ** 0.5
    except Exception as e:
        print(f"Error occurred: {e}")
        result = None

    return result

# Testing the function with valid and invalid inputs
print("The square root of 25 is:", calculate_root(25)) # This should print "The square root of 25 is: 5.0"
print()

print("The square root of -1 is:", calculate_root(-1)) # This should print "Error! Number should be non-negative."
