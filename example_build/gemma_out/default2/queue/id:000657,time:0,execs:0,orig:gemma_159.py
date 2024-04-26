
# This Python program demonstrates the use of and and exec

# Define a function called 'my_function'
def my_function(x):
    print(x)

# Use the and operator to check if x is greater than 5 and y is less than 10
if x > 5 and y < 10:
    # Execute the 'my_function' function
    exec("my_function(5)")

# Print the output
print("The value of x is:", x)
print("The value of y is:", y)
