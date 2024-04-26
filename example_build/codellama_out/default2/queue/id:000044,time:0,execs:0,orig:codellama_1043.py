x = 123
y = "abc"

# Using 'as' to convert type
print(x as str) # Output: '123'
print(y as int) # Output: 0 (because the string 'abc' cannot be converted to an integer)

# Using 'not' to check for truthiness
print(not x) # Output: False (because x is a number and numbers are always "truthy")
print(not y) # Output: True (because the string 'abc' is not empty)