import compiler

print("Hello World")

# Use None as a variable
none_var = None
print(none_var)

# Use the compiler to compile some code
code = """
print("This is a test of the compiler.")
"""
compiled_code = compiler.compile(code, mode='exec')
exec(compiled_code)