
import contextlib
import os

# Using True as a boolean value
if True:
    print("This is a true statement, it will be executed")

# Using resource module with contextlib.contextmanager decorator
@contextlib.contextmanager
def my_context_manager(file_path):
    try:
        file = open(file_path, 'r')
        yield file
    finally:
        file.close()

with my_context_manager('example.txt') as f:
    data = f.read()
    print("Data from the file:", data)
