# This program demonstrates the use of True and compile in Python

# Print "Hello, World!" to the screen
print("Hello, World!")

# Use True as an if condition
if True:
    print("True is true.")

# Compile a string into Python code
code = compile('print("Compiled code.")', '', 'exec')

# Execute the compiled code
exec(code)