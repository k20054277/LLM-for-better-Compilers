
import contextlib
import os

@contextlib.contextmanager
def open_file(filename):
    try:
        file = open(filename, 'r')
        yield file
    finally:
        if file is not None:
            file.close()

def read_file(filename):
    try:
        with open_file(filename) as f:
            content = f.read()
            print("Content of the file:", content)
    except FileNotFoundError:
        print(f"File '{filename}' does not exist.")

if __name__ == "__main__":
    filename = "example.txt"
    if os.path.exists(filename):
        read_file(filename)
    else:
        print("File not found, please create it first.")
