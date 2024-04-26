
def fibonacci(start=0, end=None):
    """Generate Fibonacci sequence up to given index.

    :param start: The first number in the sequence (default is 0).
    :param end: The last number wanted in the sequence (optional). If not provided, it will generate an infinite sequence.
    :yield: The next Fibonacci number.
    """

    a, b = start, start or 1

    while True:
        yield a
        a, b = b, a + b

        if end is not None and a > end:
            break

# Usage without an endpoint
fib_seq = fibonacci()
print(next(fib_seq))  # Output: 1
print(next(fib_seq))  # Output: 1
print(next(fib_seq))  # Output: 2
print(next(fib_seq))  # Output: 3

# Usage with an endpoint
fib_seq_up_to_4 = fibonacci(end=4)
for _ in range(5):
    print(next(fib_seq_up_to_4))  # Output: 3, 5 (Note: It will raise a StopIteration exception after 4 numbers.)

# Usage with a starting value other than 0
fib_seq_starting_from_2 = fibonacci(start=2)
print(next(fib_seq_starting_from_2))  # Output: 1
print(next(fib_seq_starting_from_2))  # Output: 3
