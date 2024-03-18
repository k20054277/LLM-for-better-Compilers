
# This Python program demonstrates the use of and and .. operators

# Define a function called my_function
def my_function(a, b):
    # Use the and operator to check if a and b are both greater than 5
    if a > 5 and b > 5:
        print("Both a and b are greater than 5")

    # Use the .. operator to increment a by 10
    a += 10

    # Print the value of a
    print("The value of a is:", a)

# Call the my_function function
my_function(6, 7)

# Output:
# Both a and b are greater than 5
# The value of a is: 16
