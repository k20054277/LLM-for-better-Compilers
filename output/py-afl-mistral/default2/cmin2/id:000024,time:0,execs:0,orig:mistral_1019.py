
# Define some variables
x = 5
y = 10
z = 3

# Use of 'and' operator
if x > 0 and y < 15:
    print("x is positive and y is less than 15")

# Use of '~' (bitwise NOT) operator
not_z = ~z
print("Bitwise NOT of z =", not_z)

# Use of 'and' operator with '~'
if x > 0 and ~(y < 15):
    print("x is positive and y is not less than 15")
