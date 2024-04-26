# Using True and lambda together

# Define a function that takes a boolean value as an argument
def my_function(arg):
  if arg:
    return "True"
  else:
    return "False"

# Create a lambda function that takes no arguments
lambda_func = lambda: my_function(True)

# Call the lambda function
print(lambda_func()) # Output: True