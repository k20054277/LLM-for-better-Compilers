# Demonstrate the use of True and global

# Define a function that uses global variables
def my_function():
    # Use global keyword to access the global variable
    global x
    print("Value of x:", x)

# Assign value to x, which is a global variable
x = 10

# Call the function and observe the output
my_function()