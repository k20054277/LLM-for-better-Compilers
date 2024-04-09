
# This Python program demonstrates the use of and and abs functions

# Define a function to demonstrate the use of and and abs
def demonstrate_and_abs(x):
    # Use the and operator to check if x is greater than 0 and less than 5
    if x > 0 and x < 5:
        # Print x is greater than 0 and less than 5
        print("x is greater than 0 and less than 5")

    # Use the abs function to find the absolute value of x
    abs_x = abs(x)
    # Print the absolute value of x
    print("The absolute value of x is:", abs_x)

# Demonstrate the use of and and abs functions
demonstrate_and_abs(3)
demonstrate_and_abs(-2)
