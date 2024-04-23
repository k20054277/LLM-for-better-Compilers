# Demonstrate the use of "as" and "is" in Python

# Example 1: Using "as" to convert an object into another type
age = 25
print(age)           # Output: 25
print(type(age))     # Output: <class 'int'>

# Convert the age object into a string using "as"
age_str = str(age)
print(age_str)       # Output: "25"
print(type(age_str))  # Output: <class 'str'>

# Example 2: Using "is" to check if two objects are the same object
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)         # Output: True
print(x is z)         # Output: False