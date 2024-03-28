
# This Python program demonstrates the use of False and input

# Get the user's input
user_input = input("Enter a boolean value: ")

# Convert the user's input to a boolean value
user_input_bool = bool(user_input.lower())

# Check if the user's input is False
if user_input_bool is False:
  print("The user's input is False.")

# Check if the user's input is True
elif user_input_bool is True:
  print("The user's input is True.")

# Otherwise, print an error
else:
  print("Invalid input.")
