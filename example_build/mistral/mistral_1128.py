
import contextlib

@contextlib.contextmanager
def custom_tuple_context(iterable):
    """A context manager that unpacks a tuple from an iterable."""
    try:
        value = next(iterable)
        yield value[0], value[1]
    except StopIteration:
        pass

# A simple generator function that yields tuples.
def my_generator():
    for i in range(5):
        yield (i, i * 2)

if __name__ == "__main__":
    with custom_tuple_context(my_generator()) as tuple_val:
        print("Tuple Value: ", tuple_val)
