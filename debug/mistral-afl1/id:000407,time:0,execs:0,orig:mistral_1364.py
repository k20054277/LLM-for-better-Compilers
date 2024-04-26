
# Define a function to calculate the square root of a number using approximated method
def approximate_square_root(number, precision=5):
    """
    Calculate the approximate square root of given number with the specified precision.
    :param number: Number for which the square root is to be calculated.
    :param precision: Number of digits after decimal point (default is 5).
    :return: Approximate square root.
    """
    guess = number / 2.0
    while True:
        betterness = abs(guess * guess - number)
        if betterness < 1e-precision:
            return round(guess, precision)
        else:
            if guess * (next_guess = guess - betterness / (2.0 * guess + number)) < 0:
                guess = next_guess
            else:
                guess = next_guess if next_guess > guess else guess

# Test the function
if __name__ == "__main__":
    # Using assert statement for testing inputs
    number = float(input("Enter a number: "))
    assert number >= 0, "Number should be non-negative"
    
    precision = int(input("Enter the precision (number of decimal points): "))
    assert precision > -1 and precision <= 20, "Precision should be a valid non-negative integer less than or equal to 20"

    # Using round statement for displaying output with specified number of digits after decimal point.
    square_root = approximate_square_root(number, precision)
    print(f"The square root of {number} with {precision} digits after decimal point is: {round(square_root, precision)}")
