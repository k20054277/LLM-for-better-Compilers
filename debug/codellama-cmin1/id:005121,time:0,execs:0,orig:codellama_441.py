# Demonstrate the use of None and bool in Python

# None represents an absent value, which is different from False
print(None)  # Output: None
print(bool(None))  # Output: False

# bool can be used to convert a variable to a boolean value
x = "hello"
y = "world"
if x == y:
    print("x and y are equal")
else:
    print("x and y are not equal")

# Convert the string "hello" to a boolean value using bool() function
bool_value = bool(x)
print(bool_value)  # Output: True

# Convert the string "world" to a boolean value using bool() function
bool_value = bool(y)
print(bool_value)  # Output: False