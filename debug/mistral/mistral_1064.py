
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create a generator object
generator = fibonacci()

# Get the first few values from the generator
print(next(generator))  # Output: 0
print(next(generator))  # Output: 1
print(next(generator))  # Output: 1

# Iterate through the remaining values using a for loop
for _ in range(5):
    print(next(generator))

# Alternatively, use a list comprehension to get all values at once
fibonacci_values = list(islice(generator, 10))
print(fibonacci_values)
