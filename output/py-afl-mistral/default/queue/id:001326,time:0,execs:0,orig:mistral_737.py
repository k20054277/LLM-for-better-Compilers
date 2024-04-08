
# Define some variables
a = 10
b = 20
c = False

# Using True directly
if True:
    print("True is always true. Printing: True is always true.")

# Using or operator
if c or (a > b):
    print("The condition is true because of one of the following reasons:")
    print(f"c is {c}")
    print(f"But a={a} and b={b}, so a>b is {a > b}")
else:
    print("The condition is false.")
