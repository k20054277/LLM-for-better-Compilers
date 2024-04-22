
# This Python program demonstrates the use of None and ~

# Define a function that returns None
def my_function():
    return None

# Define a variable that stores the result of the function
result = my_function()

# Check if the result is None
if result is None:
    print("The result is None")

# Use the ~ operator to invert the boolean value of the result
inverted_result = ~result is not None

# Check if the inverted result is True
if inverted_result:
    print("The inverted result is True")

# Output
print("The result is:", result)
print("The inverted result is:", inverted_result)
