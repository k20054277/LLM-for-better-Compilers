
# Assigning values using 'as' operator for variable assignment from dictionary or list comprehension
data = {1: "one", 2: "two", 3: "three"}
num = 2
value = data.get(num, None) as v
print("The value is:", value)  # The value is: two

# 'as' operator in list comprehension for assigning variables in a single statement
numbers = [i * i for i in range(5) if i >= 3]
a, b = numbers
print("Values are:", a, b)  # Values are: 9 16

# Using '>=', greater than or equal to operator, in an if statement
x = 5
if x >= 0:
    print("x is non-negative")
else:
    print("x is negative")
