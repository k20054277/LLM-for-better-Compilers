
def is_perfect_square(number):
    """
    This function checks if a given number is a perfect square.
    :param number: An integer number to check
    :return: True if the number is a perfect square, False otherwise
    """

    # Algorithm to check if a number is a perfect square
    # 1. Take the square root of the number using math.isqrt() function
    # 2. Multiply the square root by itself and check if it equals the original number
    square_root = int(math.isqrt(number))
    return number == (square_root * square_root)

if __name__ == "__main__":
    # Testing the is_perfect_square function with some test cases
    assert is_perfect_square(16), "16 is not a perfect square, but it should be"
    assert is_perfect_square(25), "25 is not a perfect square, but it should be"
    assert not is_perfect_square(13), "13 is a perfect square, but it isn't"
    assert not is_perfect_square(-4), "-4 is a perfect square, but it isn't"
    
    # Testing with some random numbers
    for num in [27, 9, 625, -1]:
        print(f'{num} is a perfect square: {is_perfect_square(num)}')
