# Assign None to a variable
x = None

# Check if a variable is None
if x is None:
    print("x is None")

# Use None as a default value in a function
def greet(name=None):
    if name is None:
        print("Hello, World!")
    else:
        print(f"Hello, {name}!")

# Pass None to a function as an argument
greet()