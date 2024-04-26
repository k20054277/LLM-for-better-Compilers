
# Define a dictionary with attributes and functions for a simple calculator
calc = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
}

# Use getattr() to access functions by their names as strings
for operation in ['add', 'subtract', 'multiply']:
    func = getattr(calc, operation)
    print(f"{operation} operation: {func(5, 3)}")

# Use as to assign a function to a variable directly
as_add = calc['add']
print(f"Addition using 'as': {as_add(5, 3)}")
