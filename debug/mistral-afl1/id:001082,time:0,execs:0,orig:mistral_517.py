
# Function to set a global variable
def set_global(val):
    global x
    x = val

# Function that uses a global variable
def print_x():
    global x
    print("The value of x is:", x)

# Initialize an empty list as a local variable with the same name as the global one
x = []

# Set the global variable in the function set_global
set_global(True)

# Print the local variable (which remains unchanged)
print("The value of the local x is:", x)

# Print the global variable
print_x()
