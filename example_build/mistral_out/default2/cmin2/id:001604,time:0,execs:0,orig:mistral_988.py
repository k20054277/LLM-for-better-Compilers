
# Define some variables
a = True
b = False
c = True

# Use the 'and' operator to perform a logical AND operation
result = (a and b) or c

print("Value of result: ", result)

# Let's analyze the truth table for this expression:
if a is True and b is False:
    result = False  # Since False 'and' anything is always False
else:
    result = c       # If at least one operand is True, then the result is that True value

print("When a = {0} and b = {1}:".format(a, b))
print("The expression (a and b) or c evaluates to:", result)

# Now let's change the values of 'a' and 'b' for another example:
a = False
b = True
result = (a and b) or c

print("\nWhen a = {0} and b = {1}:".format(a, b))
print("The expression (a and b) or c evaluates to:", result)
