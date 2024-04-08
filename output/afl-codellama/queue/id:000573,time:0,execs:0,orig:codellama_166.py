# Demonstrate the use of False and assert in Python

# Define a function that takes a boolean argument
def my_function(my_bool):
  # Use an if statement to check if the argument is True
  if my_bool:
    print("The argument was True")
  else:
    print("The argument was False")

# Call the function with True and False as arguments
my_function(True)  # Output: The argument was True
my_function(False) # Output: The argument was False

# Use assert to check if a condition is True
assert my_bool == True, "The condition was not True"