# Demonstrate the use of None
x = None
print(x)  # Output: None

# Demonstrate the use of compile
code = "print('Hello, world!')"
compiled_code = compile(code, '<string>', 'exec')
exec(compiled_code)  # Output: Hello, world!