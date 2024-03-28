
# Define a nested function using 'def'
def outer_function(input):
    def inner_function(add):
        result = input + add
        return result
    return inner_function

# Use 'as' to rename the returned inner function for better readability
square_plus_five = outer_function(5)  # The output is an inner function that takes one argument
print(square_plus_five(2))  # Output: 7

# Now we can use 'as' to give a more descriptive name to the returned inner function
square_and_add_five = outer_function(5) as add_five_to_square
print(square_and_add_five(3))  # Output: 8
