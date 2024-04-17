# This program demonstrates the use of False and the compiler in Python

# First, define a function that takes two arguments: a boolean value and a string
def print_boolean(bool_val, str_val):
  # If the boolean value is True, print the string followed by "is true"
  if bool_val:
    print(str_val + " is true")
  # Otherwise, print the string followed by "is false"
  else:
    print(str_val + " is false")

# Now, define a function that takes no arguments and returns False
def get_false():
  return False

# Call the first function with True as the boolean value and "This is true" as the string
print_boolean(True, "This is true")

# Call the first function with False as the boolean value and "This is false" as the string
print_boolean(False, "This is false")

# Call the second function and store its return value in a variable
false_val = get_false()

# Print the value of the variable to show that it is False
print(false_val)