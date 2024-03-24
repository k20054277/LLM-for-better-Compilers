# Example 1: Using None

print("Example 1")

# Assigning a variable to None
x = None

# Printing the value of x
print(x)

# Changing the value of x to an integer
x = 5

# Printing the value of x again
print(x)

# Changing the value of x back to None
x = None

# Printing the value of x again
print(x)


# Example 2: Garbage Collection

print("Example 2")

# Creating a list with a reference cycle
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = [a, b, c]
e = [d]

# Printing the values of a, b, and c
print(a)
print(b)
print(c)

# Printing the value of d
print(d)

# Printing the value of e
print(e)

# Breaking the reference cycle by setting one of the lists to None
a = None

# Printing the values of a, b, and c again
print(a)
print(b)
print(c)