
# Define variables with assigned values
num = 10
str_val = "Python"
list_data = [1, 2, 3, 4]
dict_data = {"key1": 1, "key2": 2}
bool_val = True

# Assign None and True to variables
none_val = None
true_val = not bool_val

print("Num: ", num)
print("String Value: ", str_val)
print("List Data: ", list_data)
print("Dictionary Data: ", dict_data)
print("Boolean Value: ", bool_val)
print("None Value: ", none_val)
print("True Value: ", true_val)

# Using None as default value in function
def greet(name=None):
    if name is None:
        print("Hello! What's your name?")
    else:
        print("Hello, " + name)

greet() # prints "Hello! What's your name?"
greet("John") # prints "Hello, John"

# Using True as condition in an if statement
if bool_val:
    print("Boolean is true")
else:
    print("Boolean is false")
