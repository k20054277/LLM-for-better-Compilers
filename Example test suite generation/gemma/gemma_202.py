
# Demonstrating use of and and globals

# Define a global variable
global_variable = 10

# Define a function that uses the global variable
def function_using_global():
  print("The value of global_variable is:", global_variable)

# Define a function that sets the global variable
def function_setting_global(new_value):
  global global_variable
  global_variable = new_value

# Use the function_using_global function
function_using_global()

# Output: The value of global_variable is: 10

# Set the global variable to a new value
function_setting_global(20)

# Use the function_using_global function again
function_using_global()

# Output: The value of global_variable is: 20
