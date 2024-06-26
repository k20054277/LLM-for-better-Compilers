
import contextlib

@contextlib.contextmanager
def custom_context(start, end):
    try:
        yield start, end
    finally:
        print(f"Context finished with start={start} and end={end}")

def my_generator(n):
    for i in range(n):
        yield i * 2

@contextlib.contextmanager
def print_values(iterable):
    value = tee(iterable)
    try:
        while True:
            value, next_value = next(value)
            yield next_value
    finally:
        print(f"Generator finished with last value={next(value)}")

def tee(iterable):
    it = iter(iterable)
    return iterfrom(it), it

def iterfrom(iter):
    while True:
        yield next(iter)

if __name__ == "__main__":
    with custom_context(1, 5) as context:
        with print_values(my_generator(5)) as generator:
            for i in range(3):
                next(generator)

    # Output: Context finished with start=1 and end=5
    # Generator finished with last value=12
