
def divide(x, y):
    """
    This function takes two arguments x and y, and returns quotient and remainder from the division of x by y
    using the divmod() function.
    :param x: dividend (integer or float)
    :param y: divisor (integer)
    :return: tuple with two elements - quotient and remainder
    """
    q, r = divmod(x, y)  # divide x by y and get the quotient and remainder as a tuple
    assert y != 0, "Error: Divisor cannot be zero"  # check if divisor is not zero using assert statement
    return q, r

if __name__ == "__main__":
    num1 = int(input("Enter the dividend: "))
    num2 = int(input("Enter the divisor: "))

    quotient, remainder = divide(num1, num2)
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")
