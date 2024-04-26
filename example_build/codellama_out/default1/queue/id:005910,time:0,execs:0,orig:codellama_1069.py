# Define a function that takes a string as input and returns its value as a float
def my_function(s):
    return float(s)

# Use eval to evaluate the string using my_function
result = eval("my_function('1.2')")
print(result) # Output: 1