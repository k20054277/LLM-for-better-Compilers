# Using "and" with boolean values
print(True and True)   # Output: True
print(True and False)  # Output: False
print(False and True)  # Output: False
print(False and False) # Output: False

# Using "and" with non-boolean values
print("hello" and "world")    # Output: world
print("hello" and 5)         # Output: 5
print("hello" and None)      # Output: None
print(None and "world")      # Output: None