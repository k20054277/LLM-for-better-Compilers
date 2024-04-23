
# Function to increment a given value if it is not None
def increment_if_not_none(value):
    if value is not None:
        value += 1
    return value

# Demonstration of using None and compound assignment operator +=
x = None
y = 5

print("Before function call:")
print("x =", x)
print("y =", y)

x = increment_if_not_none(x)
print("After first function call (with None):")
print("x =", x)
print("y =", y)

y = increment_if_not_none(y)
print("After second function call (with a number):")
print("x =", x)
print("y =", y)
