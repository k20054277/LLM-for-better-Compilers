
# Importing math module for square root calculation
import math

def square_root(number):
    """
    This function calculates the square root of a given number.
    :param number: The number for which we want to find the square root.
    :return: The square root of the given number.
    """
    result = math.sqrt(number)
    assert result * result >= number, f"Square root of {number} is not correct."
    return result

def main():
    number = 16
    square_root_result = square_root(number)
    print("The square root of", number, "is", square_root_result)

if __name__ == "__main__":
    main()
