
# This Python program demonstrates the use of and and repr

# Define a function to demonstrate the use of and and repr
def demonstrate_and_repr(a, b):
    # Use the and operator to check if a and b are both true
    if a and b:
        # Print "a and b are both true"
        print("a and b are both true")

    # Print the repr of a and b
    print("repr(a):", repr(a))
    print("repr(b):", repr(b))

# Call the function with two True values
demonstrate_and_repr(True, True)

# Call the function with one True and one False value
demonstrate_and_repr(True, False)

# Call the function with two False values
demonstrate_and_repr(False, False)
