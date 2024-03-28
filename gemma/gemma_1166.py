
# This Python program demonstrates the use of as and type

# Define a function called my_function that takes a variable as an argument
def my_function(x):
    # Use as to assign the type of the argument to a variable
    y = x as int

    # Check if the variable is an integer
    if isinstance(y, int):
        print("x is an integer")

    # Print the value of y
    print("The value of y is:", y)

# Call the function with different arguments
my_function(10)
my_function(2.5)
my_function("Hello")
