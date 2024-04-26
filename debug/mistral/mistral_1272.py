
# Assigning values using '=' (normal assignment)
a = 10
b = "apple"

# Assignment with 'as' keyword for variable renaming
(x, y) = (a, b)
a as z  # equivalent to 'z = a'

print("Value of a, x and z: ", a, x, z)  # Output: Value of a, x and z: 10 10 10

# Assignment with 'is' keyword for assigning the same object reference
c = [1, 2, 3]
d = c
e is c  # equivalent to 'e = c' but 'e' and 'c' point to the same object in memory

print("Identity of c and e: ", c is e)  # Output: Identity of c and e: True
