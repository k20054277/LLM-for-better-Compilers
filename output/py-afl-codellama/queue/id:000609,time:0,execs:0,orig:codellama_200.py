# Using False

print(False) # Output: False
print(not False) # Output: True
print(False and True) # Output: False
print(True or False) # Output: True

# Using compile

source_code = "def foo(): return 42"
compiled_function = compile(source_code, "", "exec")
exec(compiled_function)