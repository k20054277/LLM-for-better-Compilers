# Using assert
a = 10
b = 20

# Assertion will raise an error if the condition is not met
assert a < b, "a should be less than b"

# This line of code will never be executed because the assertion raised an error before it
print("This line will never be executed")

# Using compile
code = """
print("Hello from inside compiled function!")
"""

# Compile the code and assign to a variable
func = compile(code, "<string>", "exec")

# Execute the compiled function
exec(func)