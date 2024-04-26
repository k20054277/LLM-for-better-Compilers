
# Initializing variables with True values
x = True
y = True

print("Before assignment:")
print(f"x: {x}")
print(f"y: {y}")

# Assigning False value to a variable
x = False

print("\nAfter assigning x with False:")
print(f"x: {x}")

# Checking if variables hold the boolean values True or False using if-statement
if not (x and y):
    print("x or y is False")
else:
    print("Both x and y are True")

# Assigning false value to another variable
y = False

print("\nAfter assigning y with False:")
print(f"x: {x}")
print(f"y: {y}")

if not (x and y):
    print("x or y is False")
else:
    print("Both x and y are True")
