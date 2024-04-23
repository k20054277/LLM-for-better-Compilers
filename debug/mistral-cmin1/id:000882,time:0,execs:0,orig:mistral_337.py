
# Define a function that returns None as its return value
def none_function():
  return None

# Assign None to a variable
none_variable = None

# Define an object with no attributes, which is equivalent to having the attribute None
class NoneObject:
  pass

# Function to print the representation of variables using repr()
def print_repr(var):
  print("Representation of {}: {}".format(var.__class__.__name__, repr(var)))

if __name__ == "__main__":
  # Calling a function that returns None
  none_result = none_function()
  print("None function result:")
  print_repr(none_result)

  # Assigning None to a variable
  print("\nAssigning None to a variable:")
  print_repr(none_variable)

  # Creating and printing representation of a custom object with no attributes
  print("\nCreating and printing representation of a custom NoneObject:")
  none_obj = NoneObject()
  print_repr(none_obj)
