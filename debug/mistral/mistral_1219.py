
# File name: as_keyword.py

import io

def read_file(filename):
    with open(filename) as file:
        return file.read()

if __name__ == "__main__":
    filename = "example.txt"
    content = read_file(filename)
    print("Content of the file:", content)
