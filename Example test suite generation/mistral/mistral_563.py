
# Define a function with a local variable
def my_function():
    x = 42
    print("The value of x inside my_function is:", x)

# Call the function and assign the result to a variable
result = my_function()

# Print the ID and truth value of various Python objects
print("ID of the function my_function: ", id(my_function))
print("Truth value of an empty list: ", True if [] else False)
print("Truth value of an empty tuple: ", True if () else False)
print("Truth value of an empty dictionary: ", True if {} else False)
print("ID and truth value of the function result:")
print("ID: ", id(result))
print("Truth value: ", bool(result))
