
import os
import contextlib

# Function to open a file with specific mode and handle exceptions
def open_file(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()

# Decorator @contextmanager to create a context manager
@contextlib.contextmanager
def resource(value):
    try:
        yield value
    finally:
        if isinstance(value, (os.BufferedReader, os.TextIO)):
            value.close()

# Function to read lines from file
def read_lines(filename):
    with resource(open_file(filename, "r")) as file:
        for line in file:
            print(line)

if __name__ == "__main__":
    filename = "example.txt"
    if os.path.exists(filename):
        read_lines(filename)
    else:
        print(f"File '{filename}' does not exist.")
