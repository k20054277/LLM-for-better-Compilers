
def fibonacci(n):
    """A generator function that yields the first n numbers of Fibonacci sequence"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Create a generator object using the fibonacci function
fib_gen = fibonacci(10)

# Print first 5 Fibonacci numbers directly from the generator
for i in itertools.islice(fib_gen, 5):
    print(i)

# Assign each Fibonacci number to a variable using as keyword
next_num = next(fib_gen)
print("Next number is:", next_num)
next_num = next(fib_gen)
print("Next number is:", next_num)
