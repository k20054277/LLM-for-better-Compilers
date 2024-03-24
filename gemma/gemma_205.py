
# This Python program demonstrates the use of and and id operators

# Define a function to demonstrate the use of and and id operators
def demonstrate_and_id(a, b):
    # Use the and operator to check if a and b are both true
    if a and b:
        print("a and b are both true")

    # Use the id operator to get the unique identifier of a and b
    print("The ID of a is:", id(a))
    print("The ID of b is:", id(b))

# Call the demonstrate_and_id function with two variables
demonstrate_and_id(True, 10)
