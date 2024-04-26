
def fibonacci():
    # Initialize the first two numbers in the Fibonacci sequence
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

# Let's test our generator with some assertions
def test_fibonacci():
    fib = fibonacci()
    # First two numbers in the Fibonacci sequence should be 0 and 1
    assert next(fib) == 0
    assert next(fib) == 1

    # Test some more numbers from the sequence
    assert next(fib) == 1
    assert next(fib) == 2
    assert next(fib) == 3
    assert next(fib) == 5

if __name__ == "__main__":
    test_fibonacci()
