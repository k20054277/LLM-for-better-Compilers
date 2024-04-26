
import contextlib

def my_contextmanager():
    print("entering the context")

    def __enter__(self):
        print("entering the context manager")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exiting the context manager")

    return __enter__

@contextlib.contextmanager
def my_decorator(func):
    print("entering the decorator")

    def wrapper(*args, **kwargs):
        print("entering the wrapper")
        result = func(*args, **kwargs)
        print("exiting the wrapper")
        return result

    print("exiting the decorator")
    return wrapper

@my_decorator
def my_function():
    print("inside the function")

my_function()

print("Outside the function")
