
# Define two integer variables
num1 = 10
num2 = 20

# Comparison using not equal operator ( != )
if num1 != num2:
    print("num1 is not equal to num2")
else:
    print("num1 is equal to num2")

# Comparison with False
boolean_value = False
if num1 != boolean_value:
    print("num1 is not equal to False")
else:
    print("num1 is equal to False")

# Comparison using False directly in if condition
if not boolean_value:
    print("boolean_value is True, but it's actually False")
else:
    print("boolean_value is False, but it's actually True (this won't be printed)")
