
import os

def assert_file_exists(filepath):
    """Raise an AssertionError if the given file does not exist."""
    if not os.path.isfile(filepath):
        msg = f"File '{filepath}' does not exist."
        raise AssertionError(msg)

def process_file(filepath, delimiter='\t'):
    """Read a file line by line and print its contents."""
    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split(delimiter)
            print(elements)

if __name__ == "__main__":
    filepath = "example.txt"  # Replace with your file path
    assert_file_exists(filepath)  # Ensure the file exists before processing it
    process_file(filepath)
