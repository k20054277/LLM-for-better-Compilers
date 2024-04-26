
# This Python program demonstrates the use of None and debugging

# Define a function called 'my_function'
def my_function():
    # Return None
    return None

# Try to call 'my_function'
try:
    result = my_function()
    print(result)
except Exception as e:
    # Print the error
    print("Error:", e)

# Debug the program by printing the value of 'result'
print("Result:", result)
