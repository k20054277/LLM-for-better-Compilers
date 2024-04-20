# This program demonstrates the use of True and global variables in Python

def check_global():
    # Check if a variable is defined as global
    print("Is 'x' defined as global?", "x" in globals())

def set_global():
    # Set a variable as global
    global x
    x = 10

def get_global():
    # Get the value of a global variable
    return x

# Call the functions to demonstrate their use
check_global()
set_global()
print(get_global())