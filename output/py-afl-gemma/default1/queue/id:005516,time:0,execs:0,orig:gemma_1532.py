
# This Python program demonstrates the use of assert and ==

# Define a function to compare two numbers
def compare_numbers(num1, num2):
    assert num1 == num2
    print("The numbers are equal.")

# Call the function with two equal numbers
compare_numbers(5, 5)

# Call the function with two different numbers
compare_numbers(5, 6)

# Output
# The numbers are equal.
# Traceback (most recent call last):
#   File "demo.py", line 6, in compare_numbers
# AssertionError: expected <int> to be == <int>
