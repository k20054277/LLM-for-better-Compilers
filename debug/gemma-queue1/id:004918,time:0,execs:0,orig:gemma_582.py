
# None and Empty Parentheses

# None
print(None)  # Output: None

# Empty Parentheses
print(())  # Output: None

# Both None and Empty Parentheses
print(None == ())  # Output: True

# Explanation
print(None is None)  # Output: True
print(() is None)  # Output: False

# Using None and Empty Parentheses in Comparisons
if None == ():
    print("None and Empty Parentheses are Equal")  # Output: None and Empty Parentheses are Equal
