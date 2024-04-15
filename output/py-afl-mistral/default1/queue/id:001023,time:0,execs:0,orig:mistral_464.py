
# Function definition with optional parameter, using default value as None
def my_function(param1, param2=None):
    if param2 is not None:
        print("Received parameter2:", param2)

# Function call with one argument
my_function("Argument 1")

# Function call with two arguments
my_function("Argument 1", "Argument 2")

# Using * to unpack a tuple or list as function arguments
args = (None, "Argument X")
my_function(*args)
