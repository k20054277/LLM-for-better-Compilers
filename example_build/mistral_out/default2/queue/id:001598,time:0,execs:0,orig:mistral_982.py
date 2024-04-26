
# Define some variables
num1 = 5
num2 = 0
is_even = True

# Conditional statements using 'and' operator
if (num1 > 0) and (num2 != 0):
    print("Both num1 and num2 are non-zero.")
elif (num1 <= 0) or (num2 == 0):
    if num1 <= 0:
        print("num1 is non-positive.")
    if num2 == 0:
        print("num2 is zero.")
else:
    print("Unexpected conditions.")

# Let's check another condition using 'and' operator with boolean variables
if is_even and (num1 % 2 == 0):
    print(f"num1 is even.")
else:
    print(f"num1 is odd.")
