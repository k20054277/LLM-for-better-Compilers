
# Assigning variables
x = 10
y = 20
z = True

# Comparison using == (equality) operator
if x == y:
    print("x and y are equal")
else:
    print("x and y are not equal")

# Comparison using '=' (assignment) operator will always be False in this context
if x = y:
    print("This line will never be executed as '=' is used for assignment, not comparison.")

# Comparison using True value
if True:
    print("The boolean expression is true")
else:
    print("The boolean expression is false")

# Comparison between variables and True using == operator
if x == True:
    print(f"x equals the boolean value True.")
else:
    print(f"x does not equal the boolean value True.")

# Comparison between variables and True using and operator
if x or True:
    print("Either x is true or True is true, so this expression is true")
else:
    print("Both x and True are false, so this expression is false")
