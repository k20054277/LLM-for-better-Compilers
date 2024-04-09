
# Define a function with a parameter and a default parameter
def greet(name, greeting = "Hello"):
  """Prints a greeting to a person."""

  print(greeting + ", " + name)

# Call the function with different parameters
greet("John")
greet("Jane", greeting="Welcome")

# Check if a parameter is False
if greeting is False:
  print("The greeting parameter is False")

# Output
# Hello, John
# Welcome, Jane
# The greeting parameter is False
