
def square_root(number):
    """
    This function calculates the square root of given number using the math library.
    """
    try:
        result = math.sqrt(number)
        assert result * result >= number, f"Error! The number {number} does not have a real square root."
        return result
    except ValueError:
        print("Error! The given number is negative.")

number = 4
square_root_result = square_root(number)
print(f"The square root of the number {number} is: {square_root_result}")
