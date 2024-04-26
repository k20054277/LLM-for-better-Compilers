# Demonstrate the use of False and locals() in Python

def my_function():
    # Create a local variable
    x = 5
    print(f"Value of x: {x}")

    # Use False to create a new variable with the same name as an existing global variable
    False = "This is a string"
    print(f"Value of False: {False}")

    # Use locals() to retrieve all local variables
    print(locals())

my_function()