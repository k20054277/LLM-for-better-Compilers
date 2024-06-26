
# Define some sample source code
source_code = """
def add(x, y):
    return x + y
"""

# Compile the source code into an AST (Abstract Syntax Tree)
compiled_ast = compile(source_code, "<string>", "exec")

# Execute the compiled AST
exec(compiled_ast)

# Use the newly defined function 'add'
print(add(3, 4)) # Output: 7
