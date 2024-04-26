# This program demonstrates the use of as and ; in Python

name = "John"
age = 30

print("Name:", name)
print("Age:", age)

# The as keyword is used to specify a new variable name for an existing one.
# In this example, we are renaming the variable 'name' to 'full_name' using the as keyword.
full_name = name as str

# The ; character is used to separate multiple statements on the same line.
# In this example, we are assigning a value to the 'age' variable and then printing it out.
age = 30; print("Age:", age)