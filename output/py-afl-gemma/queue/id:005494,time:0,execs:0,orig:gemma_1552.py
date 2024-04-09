
# This Python program demonstrates the use of assert and not

def check_even(number):
    # Assert that number is even
    assert number % 2 == 0

    # Not assertion: number is not even
    # assert number % 2 != 0

    return number

# Test code
print(check_even(4))  # Output: 4
print(check_even(5))  # Output: Error
