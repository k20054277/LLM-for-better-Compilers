# Define a function that returns a value if it is provided, or None if it is not
def get_value(value):
    return value if value is not None else None

# Create a variable with a reference to an object
my_object = MyObject()

# Use the get_value function to retrieve the value of the variable
value = get_value(my_object)

# Check if the value is None and take appropriate action
if value is None:
    print("The value is None")
else:
    print("The value is", value)

# Use del to release the reference to the object and free up memory
del my_object