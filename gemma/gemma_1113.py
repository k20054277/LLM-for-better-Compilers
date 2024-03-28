
# This Python program demonstrates the use of as and compile

# Define a function
def hello(name):
    print("Hello, " + name)

# Compile the function into a bytecode object
hello_bytecode = compile(hello.__code__)

# Assigning the bytecode object to a new function
def hello_compiled(name):
    exec(hello_bytecode)

# Calling the compiled function
hello_compiled("John")

# Output:
# Hello, John
