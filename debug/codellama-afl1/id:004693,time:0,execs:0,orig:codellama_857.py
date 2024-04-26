# Using and() to evaluate multiple expressions at once
print(and(True, True))  # Output: True
print(and(True, False))  # Output: False
print(and(False, True))  # Output: False
print(and(False, False))  # Output: False

# Using eval() to evaluate expressions as strings
expression = "1 + 2"
result = eval(expression)
print(result)  # Output: