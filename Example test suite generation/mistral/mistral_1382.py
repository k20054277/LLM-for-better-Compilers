
import time

def is_even(number):
    """
    Check if the given number is even or not
    :param number: An integer
    :return: True if the number is even, False otherwise
    """
    return number % 2 == 0

# Testing the functionality of the 'is_even' function using assert statements
def test_is_even():
    assert is_even(4) == True, "Expected 4 to be even but got {}"
    assert is_even(6) == True, "Expected 6 to be even but got {}"
    assert is_even(-2) == True, "Expected -2 to be even but got {}"
    assert is_even(0) == True, "Expected 0 to be even but got {}"
    assert not is_even(3) == True, "Expected 3 to be odd but got {}"
    assert not is_even(5) == True, "Expected 5 to be odd but got {}"
    print("All tests passed!")

# Measuring the execution time of the 'is_even' function using the time module
def measure_time():
    number = 100000
    start_time = time.time()
    for _ in range(100):
        is_even(number)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time of 'is_even' function with number {}: {:.6f} seconds".format(number, execution_time))

# Calling the test and measurement functions
test_is_even()
measure_time()
