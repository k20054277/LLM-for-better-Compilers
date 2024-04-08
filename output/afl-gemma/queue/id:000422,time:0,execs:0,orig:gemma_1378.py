
# This Python program demonstrates the use of assert and input.

# Get the user input.
user_input = input("Enter a number: ")

# Convert the user input to an integer.
user_input_int = int(user_input)

# Assert that the user input is an integer.
assert isinstance(user_input_int, int)

# Assert that the user input is greater than 0.
assert user_input_int > 0

# Print the user input.
print("The user input is:", user_input_int)
