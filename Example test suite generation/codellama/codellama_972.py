# Demonstrating the use of "and" and "batch" in Python

# First let's create two variables with values we can work with:
x = 5
y = 10

# Now let's use "and" to check if both x and y are greater than 0:
if x > 0 and y > 0:
    print("Both x and y are greater than 0")
else:
    print("At least one of x or y is not greater than 0")

# Next let's use "batch" to check if either x or y is greater than 10:
if x > 10 or y > 10:
    print("Either x or y is greater than 10")
else:
    print("Neither x nor y is greater than 10")