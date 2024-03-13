# Test if a number is even or odd using modulo operator
def is_even(n):
    return n % 2 == 0

# Test if a number is positive or negative using comparison operators
def is_positive(n):
    return n > 0

# Demonstrate the use of True and %
print("Testing with even numbers:")
for i in range(1, 10):
    print(i, "is", "even" if is_even(i) else "odd")

print("\nTesting with positive numbers:")
for i in range(-5, 5):
    print(i, "is", "positive" if is_positive(i) else "negative")