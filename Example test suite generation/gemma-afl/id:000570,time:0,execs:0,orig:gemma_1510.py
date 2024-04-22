
# This Python program demonstrates the use of assert and scripting

# Define a function to test a condition
def is_even(num):
    return num % 2 == 0

# Scripting: Define a test case and assert its outcome
assert is_even(4)  # Expect True
assert is_even(6)  # Expect True
assert is_even(5)  # Expect False

# Print a message if all tests pass
print("All tests passed!")
