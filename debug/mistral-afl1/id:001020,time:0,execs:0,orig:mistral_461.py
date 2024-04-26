
import os
import contextlib

@contextlib.contextmanager
def open_file(filename):
    try:
        file = open(filename, 'r')
        yield file
    finally:
        if file is not None:
            file.close()

def print_file_content(filename):
    with open_file(filename) as f:
        content = f.read()
        print(f"The content of the file '{filename}' is:")
        print(content)

if __name__ == "__main__":
    filename = "example.txt"
    if os.path.exists(filename):
        print_file_content(filename)
    else:
        print(f"File '{filename}' does not exist.")
