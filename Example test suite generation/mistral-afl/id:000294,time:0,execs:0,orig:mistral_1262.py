
# Context Manager and Assignment with 'as'
import contextlib

@contextlib.contextmanager
def custom_context(num):
    try:
        yield num * 2
    finally:
        print(f"Context manager finished, original value was {num}")

with custom_context(5) as result:
    print("Result:", result)
