# Define a function that takes a Boolean argument
def my_function(x):
  if x:
    print("The value of x is True")
  else:
    print("The value of x is False")

# Call the function with a truthy and falsy value
my_function(True)   # Output: "The value of x is True"
my_function(False)  # Output: "The value of x is False"