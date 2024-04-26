
# This Python program demonstrates the use of and and id operators

# Define a function called my_function
def my_function(x, y):
    # Use the and operator to check if x and y are both greater than 5
    if x > 5 and y > 5:
        # If x and y are greater than 5, print "Both x and y are greater than 5"
        print("Both x and y are greater than 5")

    # Use the id operator to get the unique identifier of x
    print("The ID of x is:", id(x))

    # Use the id operator to get the unique identifier of y
    print("The ID of y is:", id(y))

# Call the my_function function with two arguments
my_function(6, 7)
