# Define two variables with different values
a = 5
b = 10

# Use the and operator to check if both variables are greater than 5
if a > 5 and b > 5:
    print("Both variables are greater than 5")
else:
    print("At least one variable is not greater than 5")

# Define a string with Python code in it
code = "print('Hello, World!')"

# Use the compile() function to create a code object from the string
code_object = compile(code, "", "exec")

# Execute the code object using the exec() function
exec(code_object)