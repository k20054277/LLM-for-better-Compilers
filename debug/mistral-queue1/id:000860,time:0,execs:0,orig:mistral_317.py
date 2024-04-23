
# Define a function that takes one argument, which can be either None or an integer
def my_function(input = None):
    if input is None:
        print("Input is None")
        # Set input to 0 if you want a default value when None is received
        input = 0

    if isinstance(input, int):
        print("Input is an integer: ", input)
        result = input * 2
        print("Result: ", result)

    else:
        print("Invalid input type. Expected None or Integer")

# Demonstrate the function with None
my_function(None)

# Demonstrate the function with an integer
my_function(5)
