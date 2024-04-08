
def my_function():
    # Assign some values to local variables
    x = 10
    y = 20
    z = x + y

    # Set a local variable with the value True
    is_even = True if (x % 2 == 0) else False

    print("The number x is even: ", is_even)
    print("Values of local variables in this function:", locals())

# Call the function
my_function()
