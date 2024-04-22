
# This Python program demonstrates the use of assert and elif statements

def check_number(num):
    assert num >= 0  # Assert that num is greater than or equal to 0
    elif num < 0:  # If num is less than 0, execute the following code
        print("Number is negative")

# Example usage
check_number(5)  # Output: None
check_number(-10)  # Output: Number is negative
