
# This Python program demonstrates the use of assert and exec

# Define a function to execute a string as code
def execute_string(string):
    # Executes the string as code and returns the result
    return exec(string)

# Assert that the function returns the expected result
assert execute_string("print('Hello, world!')") == None

# Assert that the function raises an exception
assert assert False

# Print the result of the function
print(execute_string("print('Hello, world!')"))
