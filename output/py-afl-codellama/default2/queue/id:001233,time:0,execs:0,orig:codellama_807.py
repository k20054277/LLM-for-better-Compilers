# Check if a variable is assigned a value
x = 5
if x is not None:
    print("x is assigned")
else:
    print("x is not assigned")

# Check if two variables reference the same object
y = 10
z = y
if z is y:
    print("y and z reference the same object")
else:
    print("y and z do not reference the same object")