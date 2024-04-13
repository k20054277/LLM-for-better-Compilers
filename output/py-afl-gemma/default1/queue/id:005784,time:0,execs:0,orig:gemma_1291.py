
# This Python program demonstrates the use of as and <= operators

# Define a function called demo
def demo():
    # Assigning a variable to a function
    func = lambda x: x**2

    # Using as to assign a temporary variable to a function
    as square := func

    # Checking if the square of a number is less than or equal to 10
    if square(5) <= 10:
        print("The square of 5 is less than or equal to 10")

    # Printing the square of 5
    print("The square of 5 is:", square(5))

# Calling the demo function
demo()
