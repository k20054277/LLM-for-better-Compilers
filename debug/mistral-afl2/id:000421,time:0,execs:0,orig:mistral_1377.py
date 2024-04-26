
import os
def check_file_exists(file_path):
    """
    Check if a file exists at the given path. Raise an AssertionError if not.

    :param file_path: The file path to check
    :raise AssertionError: If the file does not exist
    """

    # Use os.path.isfile() to check if the file exists
    if not os.path.isfile(file_path):
        # Raise an AssertionError with a custom message
        assert os.path.isfile(file_path), f"File '{file_path}' does not exist."

def process_file(file_path):
    """
    Read the contents of a file and print them out.

    :param file_path: The file path to read from
    """

    with open(file_path, 'r') as f:
        data = f.read()
        print("File contents:")
        print(data)

if __name__ == "__main__":
    file_path = "example.txt"  # Replace this with the path to your file
    check_file_exists(file_path)
    process_file(file_path)
