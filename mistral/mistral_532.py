
def infinite_sequence(start):
    current = start
    while True:
        yield current
        current += 1

# Create a generator with starting value 0
generator = infinite_sequence(0)

# Get first few values from the generator
print(next(generator))  # Output: 0
print(next(generator))  # Output: 1
print(next(generator))  # Output: 2

# Consume some more values (but not all of them)
for _ in range(5):
    print(next(generator))
