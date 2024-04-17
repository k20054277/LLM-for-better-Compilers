
# Define some variables
a = True
b = False

# Use the and operator
result1 = a and b
print("a and b:", result1)

# Interpretation: When both conditions (a and b) are true, then the and expression returns true; otherwise, it returns false.

# Use the not operator
result2 = not a
print("not a:", result2)

# Interpretation: The not operator negates (inverts) the given boolean value. So, if a is True, then not a is False; and vice versa.

# Combine and, not, and multiple conditions using parentheses for clarity
result3 = (not a) and b or a
print("(not a) and b or a:", result3)

# Interpretation: This expression evaluates to True only when a is False and b is true. Otherwise it evaluates to False.
