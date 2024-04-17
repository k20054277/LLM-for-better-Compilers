
import os

def create_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("Hello World!")
            print(f"File '{filename}' created.")
    else:
        print(f"File '{filename}' already exists.")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return None

filename = "example.txt"
create_file(filename)
data = read_file(filename)

if data is not None:
    print("Data in the file:")
    print(data)
else:
    print("File not found.")
