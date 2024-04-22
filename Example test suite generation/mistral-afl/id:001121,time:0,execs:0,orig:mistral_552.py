
# Define the input data
input_data = 'x = 5\ny = 3\nz = x + y'

# Evaluate the input data as Python code using exec
exec input_data

# Print the results
print("x =", x)
print("y =", y)
print("z =", z)

# Perform some calculations using True as a placeholder
expression = 'x > y'
if eval(expression):
    print("x is greater than y")
else:
    print("x is not greater than y")
