
# Define a function to demonstrate True and assertion
def check_even(number):
    # Return True if the number is even
    return number % 2 == 0

# Assert that the function returns True for even numbers
assert check_even(6) is True

# Assert that the function returns False for odd numbers
assert check_even(7) is False

# Print the results of the assertions
print("All assertions are successful!")
