# Define a function that takes two arguments, x and y
def my_function(x, y):
    # If x is less than or equal to 0, return None
    if x <= 0:
        return None
    # Otherwise, return the result of multiplying x by y
    else:
        return x * y

# Define a variable that stores the function
my_function = my_function(3, 4)

# Use the `and` operator to execute the function if the variable is not None
if my_function and exec(f"{my_function}"):
    print("The result of the function is:", my_function)
else:
    print("The function returned None")