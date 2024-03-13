
# Assigning None to a variable
none_value = None
print("none_value:", none_value)

# Using exec to evaluate simple Python expressions
expressions = [
    "x = 10",
    "y = 20",
    "z = x + y",
]

for expr in expressions:
    exec(expr)

print("x:", x)
print("y:", y)
print("z:", z)
