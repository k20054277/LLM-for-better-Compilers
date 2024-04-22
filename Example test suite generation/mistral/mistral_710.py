
import contextlib
import sys

# A simple context manager that prints messages when entered and exited
@contextlib.contextmanager
def print_context_manager(msg):
    print(f'Entering context manager: {msg}')
    try:
        yield
    finally:
        print(f'Exiting context manager: {msg}')

if __name__ == "__main__":
    with print_context_manager('Example'):
        if True:  # This condition is always true
            print('This statement is always executed inside the context manager')

        raise Exception('An error occurred')  # This will be caught and handled by the with statement
