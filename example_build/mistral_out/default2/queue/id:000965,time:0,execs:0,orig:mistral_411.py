
# Assigning None to variables
var1 = None
var2 = 42

# Expression with comparison using None
if var1 is None:
    print("Variable 1 is assigned None")
else:
    print("Variable 1 is not None, it has the value:", var1)

# Expression with arithmetic operation and None
result = 5 * var2 if var2 is not None else None
print("The result of expression is:", result)
