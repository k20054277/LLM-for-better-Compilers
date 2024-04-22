
import os.path

class CustomFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

def read_and_validate_lines(file):
    lines = file.readlines()

    # Validation using assert statements
    assert len(lines) > 0, "File is empty"
    assert all(line for line in lines if len(line.strip()) > 5), "Lines should be longer than 5 characters"

def process_file(filename):
    try:
        with CustomFileHandler(filename) as file:
            read_and_validate_lines(file)
            print("Valid lines found in the file:")
            for line in file.readlines():
                print(line.strip())
    except AssertionError as e:
        print("Validation error:", e)

# Test the program with a valid and an invalid file
process_file('example_valid.txt')
process_file('example_invalid.txt')
