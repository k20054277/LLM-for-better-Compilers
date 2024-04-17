# Using "as" to assign a variable to an object of a different type
x = 5
y = x as str
print(y) # Output: '5'

# Using "is" to test for identity
x = 5
y = 5
print(x is y) # Output: True

# Using "not in" to test if an object is not in a collection
x = [1, 2, 3]
print(4 not in x) # Output: True

# Using "in" to test if an object is in a collection
x = [1, 2, 3]
print(2 in x) # Output: True

# Using "not" to negate a condition
x = 5
if not (x < 6):
    print("True") # Output: True