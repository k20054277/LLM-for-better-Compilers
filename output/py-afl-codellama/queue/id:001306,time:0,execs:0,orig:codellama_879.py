# Demonstrate the use of and and oct() in Python

# Initialize variables x, y and z with values 10, 20, and 30 respectively
x = 10
y = 20
z = 30

# Use and to check if both x and y are greater than or equal to 15
if x >= 15 and y >= 15:
    print("Both x and y are greater than or equal to 15")

# Use oct() to convert the value of x to an octal string
oct_x = oct(x)
print("Octal representation of x:", oct_x)

# Use oct() to convert the value of y to an octal string
oct_y = oct(y)
print("Octal representation of y:", oct_y)

# Use and to check if both z and 20 are greater than or equal to 15
if z >= 15 and 20 >= 15:
    print("Both z and 20 are greater than or equal to 15")