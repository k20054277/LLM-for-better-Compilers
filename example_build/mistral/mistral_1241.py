
import contextlib

# Let's assume we have a simple function that raises some exceptions
@contextlib.contextmanager
def opening_and_closing_file(filename):
    try:
        file = open(filename, "r")
        yield file
    finally:
        file.close()

# Now let's create a context manager that will suppress specific exceptions
@contextlib.contextmanager
def handling_exceptions(exception_type):
    try:
        yield
    except exception_type as e:
        print(f"An error of type {exception_type.__name__} occurred: {e}")
    else:
        pass

# Let's create a function that raises an exception for demonstration purposes
def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

with opening_and_closing_file("example.txt") as file:
    data = file.readline()
    print(data)

# Now let's use our context managers to handle exceptions
with handling_exceptions(ZeroDivisionError):
    result = div(5, 0)
