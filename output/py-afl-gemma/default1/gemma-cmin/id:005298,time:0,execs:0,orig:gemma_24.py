
import contextlib

@contextlib.contextmanager
def my_context():
    print("Entering context")
    yield
    print("Leaving context")

with my_context():
    print("Inside context")

print("Outside context")
